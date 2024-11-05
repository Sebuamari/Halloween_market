from itertools import combinations

class CostumeShop:
    def __init__(self, city, name, costumes, prices):
        self.city = city
        self.name = name
        self.costumes = costumes
        self.prices = prices
        self.__income = 0

    @property
    def income(self):
        return self.__income

    @income.setter
    def income(self, new_income):
        self.__income = new_income

    def add_costume(self, costume_name, stock, price=0):
        if price <= 0:
            raise ValueError("Costume price must be greater than 0\n")
        elif stock <= 0:
            raise ValueError("Costume stock must be greater than 0\n")
        else:
            costume_exists = False
            for costume in self.costumes:
                if costume.name == costume_name:
                    old_stock = costume.stock
                    costume.stock += stock
                    self.adjust_price(costume_name, old_stock - costume.stock)
                    costume_exists = True

            if not costume_exists:
                self.costumes.append({'name': costume_name, 'stock': stock})
                self.prices.append({'name': costume_name, 'price': price})

    def adjust_price(self, costume_name, stock_change=0):
        for costume in self.prices:
            if costume['name'] == costume_name:
                # for each sold item, price changes
                costume['price'] = round(costume['price'] * (1 + stock_change / 100), 2)

    def adjust_stock(self, costume_name, quantity=1):
        for costume in self.costumes:
            if costume.name == costume_name:
                old_stock = costume.stock
                costume.stock -= quantity
                self.adjust_price(costume.name, old_stock - costume.stock)

    # Generates list of costumes from customer's wishlist that are available in the store
    def find_affordable_combo(self, customer):
        available_costumes = {
            wishlist_costume: price_info['price']
            for wishlist_costume in customer.wishlist
            for price_info in self.prices
            if any(costume.name == wishlist_costume and costume.stock > 0 for costume in self.costumes)
               and price_info['name'] == wishlist_costume
        }

        affordable_combos = []

        for r in range(1, len(available_costumes) + 1):
            for combo in combinations(available_costumes.items(), r):
                total_cost = sum(price for _, price in combo)
                if customer.check_budget(total_cost):
                    affordable_combos.append((combo, total_cost))

        return {
            "costume_shop": self.name,
            "affordable_combos": affordable_combos
        }

    def sell_costume(self, costume_name, quantity=1):
        total_cost = 0

        costume_to_buy = next((costume for costume in self.costumes if costume.name == costume_name), None)
        if costume_to_buy is None:
            raise ValueError("Costume not found\n")
        elif costume_to_buy.stock < quantity:
            raise ValueError(f"Not enough stock for \"{costume_name}\". Only {costume_to_buy.stock} available.")
        else:
            for costume in self.costumes:
                if costume.name == costume_name and costume.stock >= quantity:
                    total_cost = round([item['price'] for item in self.prices if item['name'] == costume_name][0] * quantity, 2)
                    self.income += total_cost

        return total_cost

    def adjust_stocks(self, costume_name, quantity=1):
        for costume in self.costumes:
            if costume.name == costume_name:
                self.adjust_stock(costume_name, costume.stock - quantity)

    def report_stock(self):
        print(f"    {self.name}, income: {self.income}")
        for costume in self.costumes:
            print(f"        Costume: {costume.name}, stock: {costume.stock}")