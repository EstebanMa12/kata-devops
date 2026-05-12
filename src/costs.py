from collections.abc import Iterable, Mapping
from typing import Union


def get_total(
    costs: Mapping[str, Union[int, float]],
    items: Iterable[str],
    tax: float = 0.0,
) -> float:
    subtotal = sum(float(costs[item]) for item in items if item in costs)
    total = subtotal * (1 + tax) + 1e-9
    return float(round(total, 2))
