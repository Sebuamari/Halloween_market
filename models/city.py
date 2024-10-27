from collections import Counter

class City:
    def __init__(self, name, population):
        self.name = name
        self.citizens = population
        self.population = len(population)
        self.costume_shops = []
        self.__demand = None

    def add_shop(self, shops):
        for shop in shops:
            self.costume_shops.append(shop)

    @property
    def demand(self):
        return self.__demand

    @demand.setter
    def demand(self, new_demand):
        self.__demand = new_demand

    def simulate_demand(self):
        costumes = [item.name for costume_shop in self.costume_shops for item in costume_shop.costumes]
        demand = Counter(costumes)
        total_costumes = sum(demand.values())
        self.demand = {
            item: round((count / total_costumes) * 100, 2) for item, count in demand.items()
        }

    def report(self):
        for shop in self.costume_shops:
            print(f"Costume shop: \"{shop['name']}\" ")
            for item in shop['costumes']:
                print(f"    Item: {item['name']}, Stock: {item['stock']}")