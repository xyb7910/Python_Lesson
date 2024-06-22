import time
from datetime import datetime
import pandas as pd

from learning_web3.link.main import connect_web3
from learning_web3.settings.address import pair_address, pair_abi
from learning_web3.link.main import web3

# 初始化 DataFrame
data = pd.DataFrame(columns=['timestamp', 'amount0In', 'amount1In', 'amount0Out', 'amount1Out'])

def handle_event(event):
    global data
    timestamp = web3.eth.getBlock(event['blockNumber'])['timestamp']
    dt_object = datetime.fromtimestamp(timestamp)
    event_data = {
        'timestamp': dt_object,
        'amount0In': web3.fromWei(event['args']['amount0In'], 'ether'),
        'amount1In': web3.fromWei(event['args']['amount1In'], 'ether'),
        'amount0Out': web3.fromWei(event['args']['amount0Out'], 'ether'),
        'amount1Out': web3.fromWei(event['args']['amount1Out'], 'ether'),
    }
    data = data.append(event_data, ignore_index=True)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data.set_index('timestamp', inplace=True)
    print(data.tail())  # 打印数据帧的最后几行，以检查数据


# 监听 Swap 事件
event_filter = web3.eth.filter({'fromBlock': 'latest', 'address': pair_address,
                                'topics': [web3.keccak(text='Swap(address,uint256,uint256,uint256,uint256,address)')]})
while True:
    try:
        for event in event_filter.get_new_entries():
            handle_event(event)
    except Exception as e:
        print(f"Error: {e}")
        web3 = connect_web3()
        while web3 is None:
            time.sleep(5)
            web3 = connect_web3()
        pair_contract = web3.eth.contract(address=pair_address, abi=pair_abi)
        event_filter = web3.eth.filter({'fromBlock': 'latest', 'address': pair_address, 'topics': [
            web3.keccak(text='Swap(address,uint256,uint256,uint256,uint256,address)')]})
    time.sleep(1)
