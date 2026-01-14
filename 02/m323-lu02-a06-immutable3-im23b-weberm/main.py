"""
updating
"""
products = [
    {'product': 'Apple', 'quantity': 5, 'price': 1.2},
    {'product': 'Banana', 'quantity': 2, 'price': 0.8},
    # Add more products as needed
]

new_prices2 = {
    'Apple': 0.5,
    'Banana': 0.3,
    # Add more prices as needed
}


def update_prices(products1, new_prices):
    # Update the price in the new products dictionary
    updated_products1 = []
    for product in products1:
        updated_product = product
        product_name = updated_product['product']
        if product_name in new_prices:
            updated_product['price'] = new_prices[product_name]
        updated_products1.append(updated_product)
    return updated_products1

def calculate_total(products1):
    # Calculate the total cost based on products and prices
    total = 0
    for product in products1:
        total += product['price'] * product['quantity']
    return total


if __name__ == '__main__':
    # Test your functions here
    updated_products = update_prices(products, new_prices2)
    print(products)
    print(updated_products)
    print(calculate_total(products))
    print(calculate_total(updated_products))
