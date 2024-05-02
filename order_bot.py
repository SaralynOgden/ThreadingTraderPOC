import logging
import random
import time

from order import Order
from signal_type import SignalType

signal_types = [SignalType.BUY, SignalType.SELL, SignalType.SKIP]

class OrderBot():

    symbolName: str
    counter: int
    
    def __init__(self, symbolName):
        self.symbolName = symbolName
        self.counter = 0
        print('order bot started for ' + self.symbolName)
    
    def check_for_trades(self, queue, event):
        print('started check for trades for ' + self.symbolName)
        while not event.is_set() and self.counter < 100:
            random_choice = random.randint(0, 22)
            weighted_random = 0
            if random_choice < 10:
                weighted_random = 0
            elif random_choice < 20:
                weighted_random = 1
            else:
                weighted_random = 2
            price = random.randint(1,101)
            signal_type = signal_types[weighted_random]
            logging.info("checking %s for signals", self.symbolName)
            if signal_type != SignalType.SKIP:
                order = Order(self.symbolName, signal_type, price, 0)
                queue.put(order)
                logging.info("Producer created order: %s (queue size= %d)", order, queue.qsize())
            time.sleep(1)
            self.counter += 1

        logging.info("Producer for %s received event. Exiting", self.symbolName)