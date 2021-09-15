FiriCLI
===
Simple CLI for interacting with Firi API endpoints. 
To be used out of box, or to assist with retrieving data
from the Firi trading API. 


1. pip install inquirer
   pip install pandas

2. Update config.py with required API keys

3. Run FiriCLI.py with Python 3 to start the CLI

*Firi account verified using BankID is required for access to private endpoints.*
*Contact support at support@miraiex.com for questions regarding API*



FiriCLI is made using a SDK provided by ronnyas, README:

Lightweight python SDK for the firi API (v2)

## Example usage
```python
from firi import pyfiri

firi = pyfiri()

# check if I have any active orders
if not firi.trade.orderList('BTCNOK'):
    # get latest 'ask' for BTCNOK
    currentAsk = firi.market.ticker('BTCNOK')['ask']

    if currentAsk < 150000:
        # place order if current price is within range
        firi.trade.createOrder(type='bid', market='BTCNOK',price=str(currentAsk),amount='0.005')
        print("Order placed.")
```

## How to use

See core/conf.py to configure how to output responses.

### Public API
```python
#Returns dict with the current time from API server
    firi.getTime()

#Returns list of dicts with the latest orders at chosen market
    firi.market.history('BTCNOK')

#Returns dict with lists of current bids/asks 
    firi.market.depth('BTCNOK')

#Returns dict with top bid, ask and spread
    firi.market.ticker('BTCNOK')

#Returns list with dicts of top bid, ask and spread for all available markets
    firi.market.tickers()

#Returns list of all available markets.
    firi.market.availableTickers()
```

### Private API
```python
#There will require accessKey (see core/conf.py)
    firi.acc.history(data='deposit')
    firi.acc.history(data='orders')
    firi.acc.history(data='orders', market='BTCNOK')

    firi.acc.history(data='trades')
    firi.acc.history(data='trades', year='2020')
    firi.acc.history(data='trades', year='2020', month='02')

    firi.acc.history(data='transactions')
    firi.acc.history(data='transactions', year='2020')
    firi.acc.history(data='transactions', year='2020', month='02')

#Returns dict of all addresses owned by the account
    firi.acc.addresses()

#Send an order to market. Type: 'bid' or 'ask'.
#Minimum price: 0.01, minimum amount: 0.0001
    firi.trade.createOrder(type='bid', market='BTCNOK', price='0.0123', amount='1')

#Cancel all orders
    firi.trade.cancelOrder()

#Cancel all orders at one market only, e.g BTCNOK
    firi.trade.cancelOrder(market='BTCNOK')

#Returns list with dict of all active orders
    firi.trade.orderList()

#Returns list with dict of all active orders at one market only, e.g BTCNOK
    firi.trade.orderList(market='BTCNOK')
```

