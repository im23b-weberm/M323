from main import gcd


def test_gcd():
    assert gcd([12, 15, 21]) == 3
    assert (
        gcd([14, 28]) == 14
    )  # Der GCD von zwei Zahlen, wobei die eine ein Vielfaches der anderen ist, ist die kleinere Zahl
    assert gcd([44, 11, 33, 22]) == 11  # Alle Zahlen sind Vielfache von 11
    assert gcd([7, 11, 13]) == 1  # Prime numbers
    assert gcd([40, 80, 120]) == 40
    assert gcd([1, 2, 3, 4, 5]) == 1  # Wenn 1 in der Liste ist, ist der GCD immer 1
    assert (
        gcd([17]) == 17
    )  # Nur eine Zahl in der Liste, der GCD sollte die Zahl selbst sein
