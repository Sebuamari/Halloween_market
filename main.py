from helpers import create_city
from helpers import purchase

try:
    city = create_city()
    for citizen in city.citizens:
        purchase.purchase_costumes(citizen, city.costume_shops)
        citizen.shop_report()

except AttributeError as e:
    print(f"An unexpected error occurred: {e}")