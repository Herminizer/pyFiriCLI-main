from miraiex import pyMiraiEx
import inquirer
import pandas as pd
import os
import time
from core import aesthetics as art

miraiex = pyMiraiEx()


def main():
    # Main menu, pointing to the different functions based on the users choice.
    clear_screen()
    art.menuArt()
    questions = [
        inquirer.List('menu',
                        message="MENU ",
                        choices=['Trade', 'Orderbooks','Open orders', 'Cancel orders', 'Trading History', 'Exit'],
                    ),
        ]
    menu_prompt = inquirer.prompt(questions)

    menu_select = menu_prompt['menu']

    if menu_select == "Trade":
        trade_menu()
    elif menu_select == "Orderbooks":
        select_orderbook()
    elif menu_select == "Open orders":
        open_orders()
        deposit = ""
        print(miraiex.trade.orderList(deposit))
    elif menu_select == "Cancel orders":
        cancel_menu()
    elif menu_select == "Trading History":
        trading_history()
    elif menu_select == "Exit":
        exit()
    else:
        main()


def trade_menu():

    clear_screen()
    questions = [
    inquirer.List('buysell',
                    message="Bid / Ask:",
                    choices=['Bid', 'Ask', 'Return'],
                ),
    ]
    menu_prompt = inquirer.prompt(questions)

    buysell = menu_prompt['buysell']

    if buysell == 'Bid':
        buy_menu()
    elif buysell == 'Ask': 
        sell_menu()
    else:
        main()

def buy_menu():

    clear_screen()
    questions = [
    inquirer.List('trademenu',
                    message="Select a pair to buy: ",
                    choices=['BTCNOK', 'ETHNOK', 'LTCNOK','XRPNOK', 'ADANOK', 'DAINOK', 'Return'],
                ),
    ]
    menu_prompt = inquirer.prompt(questions)

    menu_select = menu_prompt['trademenu']

    if menu_select == "Return":
        main()
    else:
        clear_screen()
        limit = input("Set price to buy at: ").lower()
        buy_amount = input("Set the amount to buy: ").lower()
        clear_screen()
        print(miraiex.trade.createOrder(type='Bid', amount=buy_amount, price=limit, market=menu_select))
        print("You have successfully bought ", buy_amount, " ", "for", limit, "NOK")
        wait()
    


def sell_menu():
    clear_screen()

    questions = [
    inquirer.List('trademenu',
                    message="Select a pair to sell: ",
                    choices=['BTCNOK', 'ETHNOK', 'LTCNOK','XRPNOK', 'ADANOK', 'DAINOK', 'Return'],
                ),
    ]
    menu_prompt = inquirer.prompt(questions)

    menu_select = menu_prompt['trademenu']

    head = menu_select[0:3]
    if menu_select == "Return":
        main()
    else:
        limit = input("Set price to sell at: ").lower()
        sell_amount = input("Set the amount to sell: ").lower()
        clear_screen()
        limit_int = float(limit)
        amount_int = float(sell_amount)
        print("Creating order...", "\nAsking price is", limit.lower(), "\nAmount: ", sell_amount.lower(), menu_select[0:3], "\nTotal", limit_int*amount_int, "NOK")
        print(miraiex.trade.createOrder(type='Ask', amount=sell_amount, price=limit, market=menu_select))
        
        wait()
    

def open_orders():
    clear_screen()
    questions = [
    inquirer.List('trademenu',
                    message="Select type of orders to cancel: ",
                    choices=['BTCNOK', 'ETHNOK', 'LTCNOK','XRPNOK', 'ADANOK', 'DAINOK', 'Return'],
                ),
    ]
    menu_prompt = inquirer.prompt(questions)

    menu_select = menu_prompt['trademenu']

    if menu_select == "Return":
        main()
    else:
        clear_screen()
        open_orders = miraiex.trade.orderList(menu_select)
        if open_orders == []:
            print("No open orders. \n\nReturning to menu...")
            time.sleep(2)
            main()
        else:
            df = pd.DataFrame(open_orders, columns=['id', 'market', 'type', 'price', 'amount', 'remaining', 'matched', 'cancelled', 'created_at'])
            df.sort_values(by='created_at')
        
            print(df.head(10))

            wait()


def trading_history():
    clear_screen()

    questions = [
    inquirer.List('trademenu',
                    message="Select a pair: ",
                    choices=['BTCNOK', 'ETHNOK', 'LTCNOK','XRPNOK', 'ADANOK', 'DAINOK', 'Return'],
                ),
    ]
    menu_prompt = inquirer.prompt(questions)

    menu_select = menu_prompt['trademenu']
    if menu_select == "Return":
        main()
    else:
        depth = miraiex.market.history(menu_select)
        df = pd.DataFrame(depth, columns=['type', 'amount', 'price', 'created_at', 'total'])
        df.sort_values(by='created_at')

        print(df.head(20))

        wait()

def cancel_menu():
    clear_screen()

    questions = [
    inquirer.List('trademenu',
                    message="Cancel orders in pair: ",
                    choices=['BTCNOK', 'ETHNOK', 'LTCNOK','XRPNOK', 'ADANOK', 'DAINOK', 'Cancel all', 'Return'],
                ),
    ]
    menu_prompt = inquirer.prompt(questions)

    menu_select = menu_prompt['trademenu']
    if menu_select == "Return":
        main()
    elif menu_select == "Cancel all":
        print(miraiex.trade.cancelOrder(market="BTCNOK"))
        print(miraiex.trade.cancelOrder(market="ETHNOK"))
        print(miraiex.trade.cancelOrder(market="LTCNOK"))
        print(miraiex.trade.cancelOrder(market="XRPNOK"))
        print(miraiex.trade.cancelOrder(market="ADANOK"))
        print(miraiex.trade.cancelOrder(market="DAINOK"))
        print("All open orders have been cancelled.")
    else:
        print(miraiex.trade.cancelOrder(market=menu_select))
        print("Open orders in market", menu_select, "have been successfully deleted")

    wait()

def select_orderbook():
    clear_screen()
    questions = [
    inquirer.List('ticker',
                    message="Select orderbook: ",
                    choices=['BTCNOK', 'ETHNOK', 'LTCNOK', 'XRPNOK', 'ADNOKA', 'DAINOK', 'Return'],
                ),
    ]
    orderbook_prompt = inquirer.prompt(questions)
    
    ob_choice = orderbook_prompt["ticker"]

    if ob_choice == "Return":
        main()
    else:
        while True:
            clear_screen()
            art.orderbookArt(ticker=ob_choice)
            depth = miraiex.market.depth(ob_choice)
            df = pd.DataFrame(depth['asks'], columns=['price', 'amount'])
            print("Asks")
            print(df.head(10))

            df = pd.DataFrame(depth['bids'], columns=['price', 'amount'])
            df.sort_values(by='price')
            print("Bids")
            print(df.head(10))
            time.sleep(5)

        
def clear_screen():
    """
    Clears out the screen if program
    is run in terminal, whether it's
    run on Linux, Windows or macOS
    :return:
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def wait():
    # Returning to the main menu, no matter what? :D 
    wait = input("Press enter to return")
    if wait or wait == "":
        main()
    else:
        main()

if __name__ == "__main__":
    main()