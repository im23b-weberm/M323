"""
multiplikation
"""
def multiply_all(*args):
    """
    Multiplies all the given numbers together and returns the product.

    Parameters:
        *args (float or int): Variable number of arguments to be multiplied.

    Returns:
        float or int: The product of all the given numbers.
    """
    # TODO: Implementiere die Funktion
    mult = 1
    for i in args:
        mult *= i
    return mult


if __name__ == '__main__':
    # Teste deine Funktion
    print(multiply_all(1, 2, 3))  # Erwarteter Output: 6
