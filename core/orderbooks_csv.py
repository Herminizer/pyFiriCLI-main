from firi import pyfiri

firi = pyfiri()

buy_orders = [list() for i in range(101)]
sell_orders = [list() for i in range(101)]

"""
Function for creating .csv-files from current orderbooks. Variable ticker is string, 'BTCNOK' e.g.
1 request /s would be sufficient, considering the amount of traffic on the Firi platform.
"""

def orberbook_csv(ticker):
    depth = firi.market.depth(ticker)
    with open('orderbook_btcnok.csv', 'w') as fil:
        for side in depth:
            fil.write(side + '\n')
        
            for order in depth[side]:
                fil.write(str(order) + '\n')
