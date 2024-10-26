from models import City, Customer, CostumeShop
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
    costume_shops = [
        CostumeShop(
            costume_shop['name'],
            costume_shop['costumes'],
            costume_shop['prices']
        ) for costume_shop in costume_shops_data
    ]

    # Creating and returning City object based on JSON data
    return City("Tbilisi", population, costume_shops)