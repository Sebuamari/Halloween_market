class CostumeShop:
    def __init__(self, city, name, costumes, prices):
        self.city = city
        self.name = name
        self.costumes = costumes
        self.prices = prices

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

    def sell_costumes(self, costume_name, quantity):
        self.costumes[costume_name] -= quantity

    def report_stock(self):
        for costume in self.costumes:
            print(f"Costume: {costume.name}, stock: {costume.stock}")