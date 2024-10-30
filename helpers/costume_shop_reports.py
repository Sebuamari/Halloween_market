def print_shop_reports(city):
    for costume_shop in city.costume_shops:
        costume_shop.report_stock()

    print()