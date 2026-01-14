"""
abschreibung
"""
def calculate_depreciation(initial_value, depreciation_rate, years):
    """
    Berechnet den Restwert einer Anlage nach einer bestimmten Anzahl von Jahren unter Berücksichtigung der jährlichen
    Abschreibung.

    Args:
    initial_value (float): Der Anfangswert der Anlage.
    depreciation_rate (float): Der jährliche Abschreibungssatz als Dezimalzahl (z.B. 0.10 für 10%).
    years (int): Die Anzahl der Jahre, für die die Abschreibung berechnet werden soll.

    Returns:
    float: Der Restwert der Anlage nach der gegebenen Anzahl von Jahren.

    Raises:
    ValueError: Wird geworfen, wenn der Abschreibungssatz nicht zwischen 0 und 1 liegt.
    ValueError: Wird geworfen, wenn die Anzahl der Jahre negativ ist.
    """
    if depreciation_rate < 0 or depreciation_rate > 1:
        raise ValueError("Der Abschreibungssatz muss zwischen 0 und 1 liegen.")

    if years < 0:
        raise ValueError("Die Anzahl der Jahre kann nicht negativ sein.")

    if years == 0:
        return initial_value

    return calculate_depreciation(initial_value * (1 - depreciation_rate), depreciation_rate, years - 1)


if __name__ == "__main__":
    print(calculate_depreciation(20000, 0.1, 5))
