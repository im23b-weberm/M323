"""
ggt
"""
def ggt(a, b):
    """
    :param a:
    :param b:
    :return: ggt
    """
    while b != 0:
        rest = a % b
        a = b
        b = rest
    return a


if __name__ == "__main__":
    zahl1 = 56
    zahl2 = 48
    resultat = ggt(zahl1, zahl2)
    print(
        f"Der GGT von {zahl1} und {zahl2} ist {resultat}"
    )  # Ausgabe: Der GGT von 56 und 48 ist 8
