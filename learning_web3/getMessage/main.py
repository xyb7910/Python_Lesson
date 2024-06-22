import json
from web3 import Web3
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 连接到 Binance Smart Chain
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

# 检查是否成功连接
if web3.is_connected():
    print("成功连接到 Binance Smart Chain")
else:
    print("连接失败")

# 定义交易对合约地址和 ABI
pair_address = "0x96CF68C3c017bE5AAD312B1B6BaB1B0DF63c5B41"

pair_abi = json.loads('''[
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": true,
                "internalType": "address",
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount0In",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount1In",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount0Out",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "amount1Out",
                "type": "uint256"
            },
            {
                "indexed": true,
                "internalType": "address",
                "name": "to",
                "type": "address"
            }
        ],
        "name": "Swap",
        "type": "event"
    }
]''')

pair_contract = web3.eth.contract(address=pair_address, abi=pair_abi)

# 定义区块范围（根据需求调整）
start_block = 0
end_block = web3.eth.block_number

# 获取 Swap 事件
swap_event = pair_contract.events.Swap.createFilter(fromBlock=start_block, toBlock=end_block)
events = swap_event.get_all_entries()

print(f"获取到 {len(events)} 个 Swap 事件")

# 处理事件数据
data = []
for event in events:
    timestamp = web3.eth.get_block(event['blockNumber'])['timestamp']
    dt_object = datetime.fromtimestamp(timestamp)
    data.append({
        'time': dt_object,
        'amount0In': web3.from_wei(event['args']['amount0In'], 'ether'),
        'amount1In': web3.from_wei(event['args']['amount1In'], 'ether'),
        'amount0Out': web3.from_wei(event['args']['amount0Out'], 'ether'),
        'amount1Out': web3.from_wei(event['args']['amount1Out'], 'ether')
    })

# 转换为 DataFrame
df = pd.DataFrame(data)

# 打印数据
print(df.head())

df.set_index('time', inplace=True)

ohlc_dict = {
    'open': df['amount0In'].resample('1D').first(),
    'high': df['amount0In'].resample('1D').max(),
    'low': df['amount0In'].resample('1D').min(),
    'close': df['amount0In'].resample('1D').last(),
}
ohlc_df = pd.DataFrame(ohlc_dict)

# 移除缺失值
ohlc_df.dropna(inplace=True)

# 绘制 K 线图
fig, ax = plt.subplots(figsize=(12, 6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(rotation=45)
plt.title('PPIG/WBNB Swap 事件 K 线图')
plt.xlabel('日期')
plt.ylabel('数量 (PPIG)')
plt.plot(ohlc_df.index, ohlc_df['open'], label='Open')
plt.plot(ohlc_df.index, ohlc_df['high'], label='High')
plt.plot(ohlc_df.index, ohlc_df['low'], label='Low')
plt.plot(ohlc_df.index, ohlc_df['close'], label='Close')
plt.legend()
plt.show()
