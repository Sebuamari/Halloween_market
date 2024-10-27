from models import City, Customer, CostumeShop, Costume
from helpers import read_json

def create_city():
    # Reading data from JSON files
    population_data = read_json('data/population.json')['population']
    costume_shops_data = read_json('data/shops.json')['costume_shops']

    # Creating objects from JSON data
    population = [
        Customer(
            citizen['name'],
            citizen['budget'],
            citizen['wishlist']
        ) for citizen in population_data
    ]

    # Creating and returning City object based on JSON data
    city = City("Tbilisi", population)

    # Creating objects from JSON data
    costumes = [
        Costume(
            costume['name'],
            costume['stock']
        ) for costume_shop in costume_shops_data for costume in costume_shop['costumes']
    ]

    costume_shops = [
        CostumeShop(
            city,
            costume_shop['name'],
            costumes,
            costume_shop['prices']
        ) for costume_shop in costume_shops_data
    ]

    city.add_shop(costume_shops)
    city.simulate_demand()
    return city
