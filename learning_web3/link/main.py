import time

from web3 import Web3
from web3.middleware import geth_poa_middleware

# 连接到 BSC 公共节点
bsc_url = "https://bsc-dataseed.binance.org/"


# web3 = Web3(Web3.HTTPProvider(bsc_url))

# 使用 Infura WebSocket 连接到 BSC 节点
# infura_ws = "wss://sepolia.infura.io/ws/v3/143d0fac11f047648fc1d94cd9e4d72e"
# 使用 Infura Https 连接到 BSC 节点
# infura_url = "https://sepolia.infura.io/v3/143d0fac11f047648fc1d94cd9e4d72e"


def connect_web3():
    # web3 = Web3(Web3.WebsocketProvider(infura_ws))
    # web3 = Web3(Web3.HTTPProvider(infura_url))
    web3 = Web3(Web3.HTTPProvider(bsc_url))

    if web3.is_connected():
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # 添加 POA 中间件
        print("成功连接到 BSC WebSocket 节点")
        return web3
    else:
        print("连接失败")
        return None


web3 = connect_web3()
while web3 is None:
    time.sleep(5)  # 等待 5 秒后重试连接
    web3 = connect_web3()

# 获取链上信息，例如当前区块号
block_number = web3.eth.block_number
print(f"Current block number: {block_number}")
