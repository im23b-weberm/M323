"""
product
"""
class Transaction:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


def update_inventory(inventory1, *transactions2):
    """Updates the inventory based on the provided transactions."""
    # TODO: Implementiere die Funktion
    for i in transactions2:
        if i.product in inventory1:
            inventory1[i.product] += i.quantity
        else:
            inventory1[i.product] = i.quantity

if __name__ == '__main__':
    # Teste deine Funktion
    inventory = {'Apfel': 10, 'Birne': 5}
    transactions = [Transaction('Apfel', 3), Transaction('Birne', -2)]
    update_inventory(inventory, *transactions)
    print(inventory)  # Erwarteter Output: {'Apfel': 13, 'Birne': 3}
