class Customer:
    def __init__(self, name, budget, wishlist):
        self.name = name
        self.__budget = budget
        self.wishlist = wishlist
        self.shopping_list = []

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, new_budget):
        self.__budget = new_budget

    def buy_costume(self, shop, costume_name, quantity=1):
        total_price = shop.sell_costume(costume_name)
        self.shopping_list.append(costume_name)
        self.budget -= total_price

    def check_budget(self, costume_price):
        return self.budget > costume_price

    def shop_report(self):
        print(f"{self.name}'s current budget is {self.budget()}")