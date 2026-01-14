import main


def test_total_with_discount():
    """Testfall für einen Warenkorb mit Rabatt."""
    basket = [{'Produkt': 'T-Shirt', 'Preis': 20}, {'Produkt': 'Hose', 'Preis': 50}]
    discount = 0.1
    assert main.calculate_total_pure(basket, discount) == 63.0


def test_total_without_discount():
    """Testfall für einen Warenkorb ohne Rabatt."""
    basket = [{'Produkt': 'T-Shirt', 'Preis': 20}, {'Produkt': 'Hose', 'Preis': 50}]
    discount = 0.0
    assert main.calculate_total_pure(basket, discount) == 70.0


def test_empty_basket():
    """Testfall für einen leeren Warenkorb."""
    basket = []
    discount = 0.1
    assert main.calculate_total_pure(basket, discount) == 0.0
