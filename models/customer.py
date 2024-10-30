from collections import Counter

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
        self.__budget = round(new_budget, 2)

    def buy_costume(self, shop, costume_name, quantity=1):
        if quantity <= 0:
            raise ValueError(f"Purchase process for \"{costume_name}\" can't be continued. Quantity of costumes to be bought must be greater than 0!")
        else:
            if costume_name not in self.shopping_list:
                total_price = shop.sell_costume(costume_name, quantity)
                self.shopping_list.append(costume_name)
                self.budget -= total_price

    def check_budget(self, costume_price):
        return self.budget > costume_price

    def shop_report(self):
        costume_counts = Counter(self.shopping_list)
        costume_summary = ', '.join([f"{costume} (x{count})" for costume, count in costume_counts.items()])

        if len(costume_summary) > 0:
            print(f"{self.name} purchased: [{costume_summary}]")
        else:
            print(f"{self.name} couldn't purchase anything")

        print(f"{self.name}'s budget after shopping is {self.budget}\n")