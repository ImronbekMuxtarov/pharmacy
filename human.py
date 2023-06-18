class Human:
    def __init__(self, name, money) -> None:
        self.name = name
        self.__money = money
    def get_money(self):
        return self.__money
    def set_money(self, price):
        self.__money -= price