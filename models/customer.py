class Customer:
    def __init__(self, name, budget, shopping_list):
        self.name = name
        self.__budget = budget
        self.shopping_list = shopping_list

    def get_budget(self):
        return self.__budget

    def buy_costume(self, shop, costume_name, quantity):
        pass

    def check_budget(self, costume_price):
        pass

    def shop_report(self):
        pass