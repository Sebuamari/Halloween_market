from helpers import create_city
from helpers import purchase

try:
    city = create_city()
    purchase.purchase_costumes(city.citizens[1], city.costume_shops)
except AttributeError as e:
    print(f"An unexpected error occurred: {e}")