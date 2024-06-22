import json

from learning_web3.link.main import web3

# PPIG/WBNB 交易对地址
pair_address = "0x96CF68C3c017bE5AAD312B1B6BaB1B0DF63c5B41"

# Uniswap V2 风格的交易对 ABI
pair_abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1In","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount0Out","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1Out","type":"uint256"},{"indexed":true,"internalType":"address","name":"to","type":"address"}],"name":"Swap","type":"event"}]')

# 初始化合约
pair_contract = web3.eth.contract(address=pair_address, abi=pair_abi)
