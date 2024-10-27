class Costume:
    def __init__(self, name, stock = 0):
        self.name = name
        self.__stock = stock

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, new_stock):
        self.__stock = new_stock