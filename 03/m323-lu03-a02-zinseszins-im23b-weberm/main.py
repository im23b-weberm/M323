"""
zinseszins
"""
def compound_interest(principal, rate, time):
    """
    Berechnet das Endguthaben einer Investition unter Berücksichtigung des Zinseszinses.

    Args:
    principal (float): Der Anfangsbetrag der Investition.
    rate (float): Der jährliche Zinssatz als Dezimalzahl (z.B. 0.05 für 5%).
    time (int): Die Laufzeit der Investition in Jahren.

    Returns:
    float: Das Endguthaben der Investition.

    Raises:
    ValueError: Wird geworfen, wenn die Laufzeit negativ ist.
    """
    # TODO: Implementieren Sie die Funktion rekursiv
    if time < 0:
        raise ValueError("Die Laufzeit kann nicht negativ sein.")

    if time == 0:
        return principal
    else:
        return compound_interest(principal * (1 + rate), rate, time - 1)

if __name__ == "__main__":
    compound_interest(1000, 0.05, 10)
