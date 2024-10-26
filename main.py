from helpers import create_city

try:
    city = create_city()
    print(city.costume_shops[0].costumes)
    print(city.costume_shops[0].prices)
    city.costume_shops[0].add_costume("Ghost", 2, 3)
    print(city.costume_shops[0].costumes)
    print(city.costume_shops[0].prices)
except Exception as e:
        print(f"An unexpected error occurred: {e}")