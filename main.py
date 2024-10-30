from helpers import create_city, purchase, print_shop_reports

try:
    city = create_city()

    print("Costume shop stocks before shopping day starts:")
    print_shop_reports(city)

    for citizen in city.citizens:
        try:
            purchase.purchase_costumes(citizen, city.costume_shops)
            citizen.shop_report()
        except ValueError as e:
            print(e)

    print("Costume shop stocks after the shopping day:")
    print_shop_reports(city)
except AttributeError as e:
    print(f"An unexpected error occurred: {e}")