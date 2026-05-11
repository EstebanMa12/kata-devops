def get_total(costs: dict, items: list, tax: float = 0.0) -> float:
    subtotal = sum(costs[item] for item in items if item in costs)
    total = subtotal * (1 + tax) + 1e-9
    return round(total, 2)
