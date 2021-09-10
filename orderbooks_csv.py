from miraiex import pyMiraiEx
import time

miraiex = pyMiraiEx()

buy_orders = [list() for i in range(101)]
sell_orders = [list() for i in range(101)]

"""
Functions for creating .csv-files from current orderbooks.
"""

def update_ltc():
    depth = miraiex.market.depth('BTCNOK')
    with open('orderbook_btcnok.csv', 'w') as fil:
        for side in depth:
            fil.write(side + '\n')
        
            for order in depth[side]:
                fil.write(str(order) + '\n')

def update_btc():
    depth = miraiex.market.depth('LTCNOK')
    with open('orderbook_ltcnok.csv', 'w') as fil:
        for side in depth:
            fil.write(side + '\n')
        
            for order in depth[side]:
                fil.write(str(order) + '\n')

def update_eth():
    depth = miraiex.market.depth('ETHNOK')
    with open('orderbook_ethnok.csv', 'w') as fil:
        for side in depth:
            fil.write(side + '\n')
        
            for order in depth[side]:
                fil.write(str(order) + '\n')

def update_ada():
    depth = miraiex.market.depth('ADANOK')
    with open('orderbook_adanok.csv', 'w') as fil:
        for side in depth:
            fil.write(side + '\n')
        
            for order in depth[side]:
                fil.write(str(order) + '\n')

def update_xrp():
    depth = miraiex.market.depth('XRPNOK')
    with open('orderbook_xrpnok.csv', 'w') as fil:
        for side in depth:
            fil.write(side + '\n')
        
            for order in depth[side]:
                fil.write(str(order) + '\n')

def update_dai():
    depth = miraiex.market.depth('DAINOK')
    with open('orderbook_dainok.csv', 'w') as fil:
        for side in depth:
            fil.write(side + '\n')
        
            for order in depth[side]:
                fil.write(str(order) + '\n')

def get_best_buy(self):
    '''
    returns (Account, price) of the highest priced buyer, breaking ties by earliest bid
    '''
def best_order():
    with open('orderbook_btcnok.csv', "r") as fil:
        for i in range(100, -1, -1):
            if len(buy_orders[i]) > 0:
                return (buy_orders[i][0], i)
        return None

while True:
    update_btc()
    #update_eth()
    #update_ltc()
    #update_ada()
    #update_xrp()
    time.sleep(1)