from miraiex import pyMiraiEx
import time

miraiex = pyMiraiEx()

buy_orders = [list() for i in range(101)]
sell_orders = [list() for i in range(101)]

"""
Function for creating .csv-files from current orderbooks.
"""

def orberbook_csv(ticker):
    depth = miraiex.market.depth(ticker)
    with open('orderbook_btcnok.csv', 'w') as fil:
        for side in depth:
            fil.write(side + '\n')
        
            for order in depth[side]:
                fil.write(str(order) + '\n')
