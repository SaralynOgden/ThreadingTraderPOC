from signal_type import SignalType

class Order():
    symbolName: str
    signal: SignalType
    price: float
    deviation: int

    def __init__(self, symbolName, signal, price, deviation):
        self.symbolName = symbolName
        self.signal = signal
        self.price = price
        self.deviation = deviation
    
    def __str__(self) -> str:
        return f'SymbolName: {self.symbolName}, Price: {self.price}, Signal: {self.signal}'