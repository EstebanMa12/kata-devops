import math
from collections.abc import Iterable, Mapping
from typing import Union


def get_total(
    costs: Mapping[str, Union[int, float]],
    items: Iterable[str],
    tax: float = 0.0,
) -> float:
    if costs is None:
        raise TypeError("costs must not be None")
    if not isinstance(costs, Mapping):
        raise TypeError("costs must be a mapping")
    if items is None:
        raise TypeError("items must not be None")
    if isinstance(items, (str, bytes)):
        raise TypeError("items must be a sequence of names, not str or bytes")

    try:
        tax_f = float(tax)
    except (TypeError, ValueError):
        tax_f = 0.0
    if not math.isfinite(tax_f):
        tax_f = 0.0

    subtotal = 0.0
    for item in items:
        try:
            if item not in costs:
                continue
            price = float(costs[item])
        except (TypeError, ValueError, KeyError):
            continue
        if not math.isfinite(price):
            continue
        subtotal += price

    total = subtotal * (1 + tax_f) + 1e-9
    return float(round(total, 2))
