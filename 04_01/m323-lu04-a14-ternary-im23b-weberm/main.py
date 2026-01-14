"""
rabatt
"""
def calculate_discount(price, is_on_sale):
    """
    Berechnet den Preis eines Produkts nach Rabatt.

    Args:
    price (float): Der ursprüngliche Preis des Produkts.
    is_on_sale (bool): Gibt an, ob das Produkt im Angebot ist oder nicht. Falls im Angebot, wird 10% Rabatt berechnet.

    Returns:
    float: Der Preis des Produkts nach Rabatt.
    """
    # TODO: Implementieren Sie die Funktion
    return price * 0.9 if is_on_sale is True else price


if __name__ == "__main__":
    products = [
        {"name": "Laptop", "price": 1000.0, "is_on_sale": True},
        {"name": "Maus", "price": 50.0, "is_on_sale": False},
        {"name": "Tastatur", "price": 70.0, "is_on_sale": True},
    ]

    for product in products:
        discounted_price = calculate_discount(product["price"], product["is_on_sale"])
        print(
            f"Produkt: {product['name']}, Originalpreis: {product['price']} Fr., Rabattierter Preis: {discounted_price}"
            f" Fr."
        )
