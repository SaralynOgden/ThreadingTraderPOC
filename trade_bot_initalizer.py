from flask import Response
from pool_manager import PoolManager
from order_bot import OrderBot
# from trade_executor import TradeExecutor

class TradeBotInitializer():
    counter = 0
    symbol_names = ["crm", "msft", "bby"]
    
    def start_trade_bot(self):
        pool_manager = PoolManager()
        if self.counter < len(self.symbol_names):
            print('starting trade bot')
            order_bot = OrderBot(self.symbol_names[self.counter])
            pool_manager.pool.submit(order_bot.check_for_trades, pool_manager.pipeline, pool_manager.event)
            print('submitted to pool for ' + self.symbol_names[self.counter])
            self.counter += 1
        return Response("{'a':'b'}", status=201, mimetype='application/json')