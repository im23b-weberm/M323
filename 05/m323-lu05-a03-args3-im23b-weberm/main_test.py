from main import update_inventory, Transaction


def test_update_inventory_single_transaction():
    inventory = {'Apfel': 10, 'Birne': 5}
    transactions = [Transaction('Apfel', 3)]
    update_inventory(inventory, *transactions)
    assert inventory == {
        'Apfel': 13,
        'Birne': 5,
    }, 'Should update the inventory for a single transaction'


def test_update_inventory_multiple_transactions():
    inventory = {'Apfel': 10, 'Birne': 5}
    transactions = [Transaction('Apfel', 3), Transaction('Birne', -2)]
    update_inventory(inventory, *transactions)
    assert inventory == {
        'Apfel': 13,
        'Birne': 3,
    }, 'Should update the inventory for multiple transactions'


def test_update_inventory_new_product():
    inventory = {'Apfel': 10}
    transactions = [Transaction('Birne', 5)]
    update_inventory(inventory, *transactions)
    assert inventory == {
        'Apfel': 10,
        'Birne': 5,
    }, 'Should add a new product to the inventory'


def test_update_inventory_no_transactions():
    inventory = {'Apfel': 10, 'Birne': 5}
    transactions = []
    update_inventory(inventory, *transactions)
    assert inventory == {
        'Apfel': 10,
        'Birne': 5,
    }, 'Should keep the inventory unchanged when no transactions are passed'
