from itertools import combinations

def filter_best_combos(best_combos):
    # Filter for combos with more than one costume
    filtered_combos = [
        (store, combo)
        for store, combo in best_combos
        if len(combo[0]) > 1
    ]

    # If no multi-costume combos are found, return best_combo as it is
    return filtered_combos if filtered_combos else best_combos

def filter_combos_price_based(best_combos):
    cheapest_costumes = {}

    for costume_store, (costumes, total_cost) in best_combos:
        for costume_name, costume_price in costumes:
            if costume_name not in cheapest_costumes or costume_price < cheapest_costumes[costume_name][1]:
                cheapest_costumes[costume_name] = (costume_store, costume_price)

    filtered_combinations = []
    for costume_store, (costumes, total_cost) in best_combos:
        filtered_costumes = [(name, price) for name, price in costumes if cheapest_costumes[name][0] == costume_store]
        if filtered_costumes:
            filtered_combinations.append((costume_store, (tuple(filtered_costumes), total_cost)))

    return filtered_combinations

# If we have multiple combinations from the same store, we keep only the last one
def filter_combos_store_based(filtered_best_combos):
    filtered_combos = []
    store_names = []
    for store, data in reversed(filtered_best_combos):
        if store not in store_names:
            store_names.append(store)
            filtered_combos.append((store, data))

    return filter_combos_price_based(filtered_combos)

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

    filtered_best_combos = filter_best_combos(best_combo)
    filtered_best_combos = filter_combos_store_based(filtered_best_combos)
    best_combo_details = [(shop_name, items, cost) for shop_name, (items, cost) in filtered_best_combos]
    return best_combo_details, best_total_cost

def purchase_costumes(customer, costume_shops):
    best_purchase_combo = find_best_purchase_combo(customer, costume_shops)[0]
    print(f"{customer.name} starts shopping with budget of {customer.budget}")

    for purchase in best_purchase_combo:
        for costume_shop in costume_shops:
            if costume_shop.name == purchase[0]:
                for costume in purchase[1]:
                    customer.buy_costume(costume_shop, costume[0])

    for purchase in best_purchase_combo:
        for costume_shop in costume_shops:
            if costume_shop.name == purchase[0]:
                for costume in purchase[1]:
                    costume_shop.adjust_stock(costume[0])