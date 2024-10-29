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

    def add_costume(self, costume_name, stock, price):
        costume_exists = False
        for costume in self.costumes:
            if costume.get('name') == costume_name:
                costume.stock += stock
                costume_exists = True

        for costume in self.prices:
            if costume.get('name') == costume_name:
                costume['price'] = (costume['price'] + price) / 2

        if not costume_exists:
            self.costumes.append({'name': costume_name, 'stock': stock})
            self.prices.append({'name': costume_name, 'price': price})

    def adjust_price(self, costume_name, new_price):
        self.prices[costume_name] = new_price

    def adjust_stock(self, costume_name, new_stock):
        self.costumes[costume_name] = new_stock

    def adjust_demand(self, costume_name, population):
        pass

    def generate_new_demand(self, old_price):
        pass

    def find_affordable_combo(self, wishlist, budget):
        available_costumes = {
            wishlist_costume: price_info['price']
            for wishlist_costume in wishlist
            for price_info in self.prices
            if
                any(costume.name == wishlist_costume for costume in self.costumes)
                and price_info['name'] == wishlist_costume
        }

        affordable_combos = []

        for r in range(1, len(available_costumes) + 1):
            for combo in combinations(available_costumes.items(), r):
                total_cost = sum(price for _, price in combo)
                if total_cost <= budget:
                    affordable_combos.append((combo, total_cost))

        return {
            "costume_shop": self.name,
            "affordable_combos": affordable_combos
        }

    def sell_costume(self, costume_name, quantity=1):
        for costume in self.costumes:
            if costume.name == costume_name:
                costume.stock -= quantity

        return [item['price'] for item in self.prices if item['name'] == costume_name][0] * quantity

    def report_stock(self):
        for costume in self.costumes:
            print(f"Costume: {costume.name}, stock: {costume.stock}")