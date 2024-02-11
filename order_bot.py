import logging
import random

from order import Order
from signal_type import SignalType

signal_types = [SignalType.BUY, SignalType.SELL, SignalType.SKIP]

class OrderBot():

    symbolName: str
    
    def __init__(self, symbolName):
        self.symbolName = symbolName
    
    def check_for_trades(self, queue, event):
        while not event.is_set():
            random_choice = random.randint(0, 2)
            price = random.randint(1,101)
            signal_type = signal_types[random_choice]
            logging.info("checking for %s signal", self.symbolName)
            if signal_type != SignalType.SKIP:
                order = Order(self.symbolName, signal_type, price, 0)
                logging.info("Producer creating order: %s", order)
                queue.put(order)

        logging.info("Producer received event. Exiting")