import threading
from flask import Flask
from flask_cors import CORS
from trade_bot_initalizer import TradeBotInitializer

class WebService():

    trade_bot_initializer: TradeBotInitializer

    def __init__(self, name) -> None:
        self.trade_bot_initializer = TradeBotInitializer()

        self.app = Flask(name)
        CORS(self.app)

        self.app.add_url_rule("/add_symbol", view_func=self.add_symbol) 
        self.flask_thread = threading.Thread(target=self.thread_proc)
        self.flask_thread.daemon = True

    def run(self):
        self.flask_thread.start()

    def add_symbol(self):
        return self.trade_bot_initializer.start_trade_bot()
    
    def thread_proc(self):
        self.app.run("localhost", 5000)