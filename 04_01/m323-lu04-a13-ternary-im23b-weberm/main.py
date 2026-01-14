"""
oneliner
"""
def absolute_value(num):
    """
    Berechnet den absoluten Wert einer gegebenen Zahl unter Verwendung des Ternären Operators.

    Args:
    - num (float): Die Zahl, deren absoluter Wert berechnet werden soll.

    Returns:
    - float: Der absolute Wert der gegebenen Zahl.
    """
    # TODO: Implementieren Sie die Funktion
    return num if num >= 0 else -num


# Zum Testen
if __name__ == '__main__':
    print(absolute_value(-5.5))  # Erwartete Ausgabe: 5.5
    print(absolute_value(0))  # Erwartete Ausgabe: 0
    print(absolute_value(3.14))  # Erwartete Ausgabe: 3.14
