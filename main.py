from helpers import create_city, purchase

try:
    city = create_city()

    print("Costume shop stocks before shopping day starts:")
    city.report()

    for citizen in city.citizens:
        try:
            purchase.purchase_costumes(citizen, city.costume_shops)
            citizen.shop_report()
        except Exception as e:
            print(e)

    print("Costume shop stocks after the shopping day:")
    city.report()
except AttributeError as e:
    print(f"An unexpected error occurred: {e}")