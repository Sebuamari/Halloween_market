import random

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

    def count_demand(self):
        costumes = set([item.name for costume_shop in self.costume_shops for item in costume_shop.costumes])

        demand = {}
        for costume in costumes:
            for citizen in self.citizens:
                for wishlist_costume in citizen.wishlist:
                    if costume == wishlist_costume:
                        demand[costume] = demand.get(costume, 0) + 1

        self.demand = demand

    def simulate_demand(self):
        costumes = [item.name for costume_shop in self.costume_shops for item in costume_shop.costumes]

        random_costumes = random.sample(costumes, random.choice([1,2])) # randomly choosing 1 or 2 costumes
        random_citizens = random.sample(self.citizens, random.choice([1,len(self.citizens)])) # randomly choosing citizens of the city

        # updating citizens' wishlists and updating demand
        for citizen in random_citizens:
            for costume in random_costumes:
                if costume not in citizen.wishlist:
                    citizen.wishlist.append(costume)

        self.count_demand()

    def report(self):
        for shop in self.costume_shops:
            print(f"Costume shop: \"{shop.name}\", income: {shop.income} ")
            for item in shop.costumes:
                print(f"    Item: {item.name}, Stock: {item.stock}")