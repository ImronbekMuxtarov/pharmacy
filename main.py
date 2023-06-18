import datetime
from human import Human
from drug import Drug
# print(str(datetime.datetime.now()).split(' ')[0]) 
class Pharmasy:
    def __init__(self, name, location, cash) -> None:
        self.name = name
        self.location = location
        self.__cash = 100
        self.drug_dct = {}
    def add_drug(self, drug : Drug):
        if drug.name in self.drug_dct:
            self.drug_dct[drug.name][0] += 1
        else:
            self.drug_dct[drug.name] = [1, drug.price, drug.expiredate]
    def remove_drug(self, drug : Drug):
        self.drug_dct.pop(drug.name)
    def sell_drug(self, drug : Drug, human : Human):
        if human.get_money() >= drug.price:
            human.set_money(drug.price)
            self.__cash += drug.price
            print("Koproq keb turing kasal bolib xayr")
        else:
            print('Pulingiz yetmadi!')
    def info(self):
        print(f'''Name: {self.name}
            Location: {self.location}''')
drug = Drug("parasetamol", 12000)
