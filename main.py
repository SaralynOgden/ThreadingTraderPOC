import concurrent.futures
import logging
import queue
import threading
import time

from order_bot import OrderBot
from trade_executor import TradeExecutor

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

pipeline = queue.Queue(maxsize=10)
event = threading.Event()
trade_executor = TradeExecutor()

with concurrent.futures.ThreadPoolExecutor() as executor:
    print('Welcome to BBS Trader!')
    start_trading = False
    symbol_names = []
    while not start_trading:
        print('Enter the name of the symbol you would like to trade on: ')
        symbol_names.append(input())
        print('Would you like to keep adding symbols to trade on? (y/n)')
        answer = input()
        while answer != 'y' and answer != 'n':
            print("Response must be y or n. Try again: ")
            answer = input()
        start_trading = answer == 'n'
        
    for symbol_name in symbol_names:
        order_bot = OrderBot(symbol_name)
        executor.submit(order_bot.check_for_trades, pipeline, event)

    executor.submit(trade_executor.execute_trades, pipeline, event)

    time.sleep(0.1)
    logging.info("Main: about to set event")
    event.set()