import pytest
from src.costs import get_total


class TestCosts:
    def test_basic_case(self):
        costs = {"socks": 5, "shoes": 60, "sweater": 30}
        assert get_total(costs, ["socks", "shoes"], 0.09) == pytest.approx(70.85)

    def test_unknown_item_ignored(self):
        costs = {"socks": 5, "shoes": 60}
        assert get_total(costs, ["socks", "hat"], 0.00) == pytest.approx(5.00)

    def test_empty_list(self):
        costs = {"socks": 5, "shoes": 60}
        assert get_total(costs, [], 0.09) == pytest.approx(0.00)

    def test_zero_tax(self):
        costs = {"a": 10, "b": 20}
        assert get_total(costs, ["a", "b"], 0.00) == pytest.approx(30.00)

    def test_all_unknown(self):
        costs = {"x": 1}
        assert get_total(costs, ["y", "z"], 0.05) == pytest.approx(0.00)

    def test_multiple_entries(self):
        costs = {"a": 10, "b": 20}
        assert get_total(costs, ["a", "b"], 0.05) == pytest.approx(31.50)
