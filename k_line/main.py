from web3 import Web3
from web3.middleware import geth_poa_middleware
from datetime import datetime
import time
import threading
import pandas as pd
import matplotlib.pyplot as plt

bsc_url = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc_url))

web3.middleware_onion.inject(geth_poa_middleware, layer=0)

if web3.is_connected():
    print("Successfully connected to Binance Smart Chain")
else:
    print("Failed to connect to Binance Smart Chain")

token_address = Web3.to_checksum_address("0xa350fb144b78486be8c86499c3348fca1fde71fb")
pair_address = Web3.to_checksum_address("0x96cf68c3c017be5aad312b1b6bab1b0df63c5b41")

# PPIG/WBNB 交易对合约的 ABI
pair_abi = '''
[
    {
        "anonymous": false,
        "inputs": [
            {"indexed": true, "name": "sender", "type": "address"},
            {"indexed": false, "name": "amount0In", "type": "uint256"},
            {"indexed": false, "name": "amount1In", "type": "uint256"},
            {"indexed": false, "name": "amount0Out", "type": "uint256"},
            {"indexed": false, "name": "amount1Out", "type": "uint256"},
            {"indexed": true, "name": "to", "type": "address"}
        ],
        "name": "Swap",
        "type": "event"
    }
]
'''

# 创建交易对合约实例
pair_contract = web3.eth.contract(address=pair_address, abi=pair_abi)

# 创建 Swap 事件过滤器
swap_event_filter = pair_contract.events.Swap.create_filter(fromBlock='latest')

# 初始化 DataFrame
data = {
    'timestamp': [],
    'price': [],
    'volume': []
}
df = pd.DataFrame(data)


def handle_event(event):
    global df

    # 提取事件数据
    timestamp = web3.eth.get_block(event['blockNumber'])['timestamp']
    dt_object = datetime.fromtimestamp(timestamp)
    amount0In = web3.from_wei(event['args']['amount0In'], 'ether')
    amount1In = web3.from_wei(event['args']['amount1In'], 'ether')
    amount0Out = web3.from_wei(event['args']['amount0Out'], 'ether')
    amount1Out = web3.from_wei(event['args']['amount1Out'], 'ether')

    # 计算价格和交易量（此处假设 amount0 是代币，amount1 是 WBNB）
    if amount0In > 0:
        price = amount1In / amount0In
        volume = amount0In
    else:
        price = amount1Out / amount0Out
        volume = amount0Out

    # 添加数据到 DataFrame
    new_data = pd.DataFrame({
        'timestamp': [dt_object],
        'price': [price],
        'volume': [volume]
    })

    # 排除空或全 NA 条目
    if not new_data.isna().all(axis=None):
        df = pd.concat([df, new_data], ignore_index=True)

    # 根据具体需求处理数据，这里只是打印出来
    print(f"Time: {dt_object}, price: {price}, volume: {volume}")


# 轮询新事件
def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)


thread = threading.Thread(target=log_loop, args=(swap_event_filter, 2), daemon=True)
thread.start()


# 绘制 K 线图
def plot_ohlc(df):
    # 生成 K 线图
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['price'], marker='o')
    plt.title('PPIG/WBNB Price')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.grid()
    plt.show()


# 定时绘制 K 线图
def plot_loop(interval):
    while True:
        if not df.empty:
            plot_ohlc(df)
        time.sleep(interval)


plot_thread = threading.Thread(target=plot_loop, args=(60,), daemon=True)
plot_thread.start()

# 保持主线程运行
while True:
    time.sleep(10)
