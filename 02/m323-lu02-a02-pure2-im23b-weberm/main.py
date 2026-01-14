"""
e-commerce
"""
BASKET = [{'Produkt': 'T-Shirt', 'Preis': 20}, {'Produkt': 'Hose', 'Preis': 50}]
DISCOUNT = 0.1


# Unpure function
def calculate_total_unpure():
    """
    Berechnet den Gesamtpreis basierend auf globalen Variablen (unpure).
    """
    total2 = sum(item['Preis'] for item in BASKET)
    discount = total2 * DISCOUNT
    total = total2 - discount
    print(f'Gesamtpreis: {total}')
    return total


# Pure function
def calculate_total_pure(basket, discount):
    """
    Berechnet den Gesamtpreis eines Warenkorbs mit einem Rabatt (pure function).
    """
    total3 = sum(item['Preis'] for item in basket)
    discounting = 1 - discount
    discounted = total3 * discounting
    return discounted


if __name__ == '__main__':
    print('Unpure function:')
    calculate_total_unpure()

    print('Pure function:')
    total4 = calculate_total_pure(BASKET, DISCOUNT)
    print(f'Gesamtpreis: {total4}')
