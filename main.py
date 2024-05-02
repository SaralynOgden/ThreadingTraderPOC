import logging
import queue
import threading

from pool_manager import PoolManager
from trade_executor import TradeExecutor
from api.web_service import WebService

format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                    datefmt="%H:%M:%S")

pipeline = queue.Queue(maxsize=10)
event = threading.Event()
trade_executor = TradeExecutor()

# FLASK. This runs on a seperate (daemon) thread
ws = WebService(__name__)
ws.run()

pool_manager = PoolManager()
pool_manager.pool.submit(trade_executor.execute_trades, pool_manager.pipeline, pool_manager.event)



print('Enter the name of the symbol you would like to trade on: ')
input()

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     print('Welcome to BBS Trader!')
#     start_trading = False
#     symbol_names = []
#     while not start_trading:
#         print('Enter the name of the symbol you would like to trade on: ')
#         symbol_names.append(input())
#         print('Would you like to keep adding symbols to trade on? (y/n)')
#         answer = input()
#         while answer != 'y' and answer != 'n':
#             print("Response must be y or n. Try again: ")
#             answer = input()
#         start_trading = answer == 'n'
        
#     for symbol_name in symbol_names:
#         order_bot = OrderBot(symbol_name)
#         executor.submit(order_bot.check_for_trades, pipeline, event)

#     executor.submit(trade_executor.execute_trades, pipeline, event)

#     time.sleep(0.5)
#     logging.info("Main: about to set event")
#     event.set()