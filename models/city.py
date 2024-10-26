from collections import Counter

class City:
    def __init__(self, name, population, costume_shops):
        self.name = name
        self.citizens = population
        self.population = len(population)
        self.costume_shops = costume_shops

    def add_shop(self, shop):
        self.costume_shops.append(shop)

    def simulate_demand(self):
        costumes = [item['name'] for costume_shop in self.costume_shops for item in costume_shop['costumes']]
        demand = Counter(costumes)
        total_costumes = sum(demand.values())
        return {
            item: round((count / total_costumes) * 100, 2) for item, count in demand.items()
        }

    def report(self):
        for shop in self.costume_shops:
            print(f"Costume shop: \"{shop['name']}\" ")
            for item in shop['costumes']:
                print(f"    Item: {item['name']}, Stock: {item['stock']}")