"""
multiplymu
"""
def create_multiplier(multiplier):
    """
    Erstellt eine innere Funktion, die Zahlen mit dem angegebenen Multiplikator multipliziert.

    Args:
        multiplier (int or float): Der Multiplikator, mit dem die Zahlen multipliziert werden sollen.

    Returns:
        function: Eine innere Funktion, die eine Zahl akzeptiert und sie mit dem Multiplikator multipliziert.
    """
    # TODO: Implementiere die Multiplikation
    def multiply(multiplier2):
        return multiplier * multiplier2
    return multiply

if __name__ == '__main__':
    multiply_by_three = create_multiplier(3)
    print(multiply_by_three(4))  # Erwarteter Output: 12
