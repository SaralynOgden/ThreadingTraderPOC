import logging

class TradeExecutor():

    def execute_trades(self, queue, event):
        while not event.is_set() or not queue.empty():
            if not queue.empty():
                order = queue.get()
                logging.info(
                    "Consumer processing order: %s (queue size=%d)", order, queue.qsize()
                )

        logging.info("Consumer received event. Exiting")