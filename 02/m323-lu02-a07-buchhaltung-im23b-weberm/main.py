"""
transakting
"""
# Dein Code kommt hier hin

def add_transaction(trans, new_trans):

    return trans + (new_trans, )

def calculate_balance(transa):
    balance = 0
    for transac in transa:
        typ, amount = transac
        if typ == "Deposit":
            balance += amount
        if typ == "Withdrawal":
            balance -= amount
    return balance
if __name__ == "__main__":
    # Dein Code kommt hier hin
    pass
