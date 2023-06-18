from datetime import datetime as d
class Drug:
    def __init__(self, name,  price) -> None:
        self.name = name
        self.expiredate = str(d.now()).split()[0]
        self.price = price
    def info(self):
        return f"Nomi: {self.name}\nYaroqlilik muddati; {self.expiredate}\nNarxi: {self.price}"
    