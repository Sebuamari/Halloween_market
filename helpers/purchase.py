from itertools import combinations

def find_best_purchase_combo(customer, costume_shops):
    best_combos = []

    for costume_shop in costume_shops:
        affordable_combos = costume_shop.find_affordable_combo(customer)
        for combo in affordable_combos['affordable_combos']:
            best_combos.append((costume_shop.name, combo))

    best_combo = []
    best_total_cost = float('inf')
    best_count = 0

    for r in range(1, len(best_combos) + 1):
        for combo in combinations(best_combos, r):
            total_cost = sum(cost for _, (_, cost) in combo)
            total_items = sum(len(items) for _, (items, _) in combo)

            if total_cost <= customer.budget:
                if (total_items > best_count) or (total_items == best_count and total_cost < best_total_cost):
                    best_combo = combo
                    best_total_cost = total_cost
                    best_count = total_items

    best_combo_details = [(shop_name, items, cost) for shop_name, (items, cost) in best_combo]
    return best_combo_details, best_total_cost

def purchase_costumes(customer, costume_shops):
    best_purchase_combo = find_best_purchase_combo(customer, costume_shops)[0]

    for purchase in best_purchase_combo:
        for costume_shop in costume_shops:
            if costume_shop.name == purchase[0]:
                for costume in purchase[1]:
                    customer.buy_costume(costume_shop, costume[0])

    for purchase in best_purchase_combo:
        for costume_shop in costume_shops:
            if costume_shop.name == purchase[0]:
                for costume in purchase[1]:
                    costume_shop.adjust_stocks(costume[0])