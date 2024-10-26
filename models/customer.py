class Customer:
    def __init__(self, name, budget, wishlist):
        self.name = name
        self.__budget = budget
        self.wishlist = wishlist
        self.shopping_list = []

    def get_budget(self):
        return self.__budget

    def buy_costume(self, shop, costume_name, quantity):
        pass

    def check_budget(self, costume_price):
        return self.get_budget() > costume_price

    def shop_report(self):
        print(f"{self.name}'s current budget is {self.get_budget()}")