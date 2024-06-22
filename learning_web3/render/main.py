import time

import matplotlib.pyplot as plt
import mplfinance as mpf
import threading

from learning_web3.link.main import connect_web3
from learning_web3.swapdata.main import data, handle_event
from learning_web3.settings.address import pair_address, pair_abi
from learning_web3.link.main import web3

# 初始化图表
fig, ax = plt.subplots()


def update_plot():
    while True:
        if not data.empty:
            df_ohlc = data.resample('1Min').agg({
                'amount0In': 'sum',
                'amount1In': 'sum',
                'amount0Out': 'sum',
                'amount1Out': 'sum'
            })

            if not df_ohlc.empty:
                df_ohlc.rename(columns={
                    'amount0In': 'open',
                    'amount1In': 'high',
                    'amount0Out': 'low',
                    'amount1Out': 'close'
                }, inplace=True)

                ax.clear()
                mpf.plot(df_ohlc, type='candle', style='charles', ax=ax)
                plt.pause(60)
            else:
                print("没有聚合数据来绘制K线图")
        else:
            print("数据帧为空")
        time.sleep(60)  # 每分钟更新一次


# 启动图表更新线程
thread = threading.Thread(target=update_plot)
thread.start()

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
