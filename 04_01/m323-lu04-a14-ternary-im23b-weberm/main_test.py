from main import calculate_discount


def test_calculate_discount():
    # Testfälle für Produkte, die im Angebot sind
    assert calculate_discount(100.0, True) == 90.0  # 10% Rabatt auf 100Fr. ist 90Fr.
    assert calculate_discount(50.0, True) == 45.0  # 10% Rabatt auf 50Fr. ist 45Fr.
    assert calculate_discount(200.0, True) == 180.0  # 10% Rabatt auf 200Fr. ist 180Fr.

    # Testfälle für Produkte, die nicht im Angebot sind
    assert calculate_discount(100.0, False) == 100.0  # Kein Rabatt, also 100Fr.
    assert calculate_discount(50.0, False) == 50.0  # Kein Rabatt, also 50Fr.
    assert calculate_discount(200.0, False) == 200.0  # Kein Rabatt, also 200Fr.

    # Testfälle mit Sonderwerten
    assert (
        calculate_discount(0.0, True) == 0.0
    )  # 10% Rabatt auf 0Fr. ist immer noch 0Fr.
    assert calculate_discount(0.0, False) == 0.0  # Kein Rabatt auf 0Fr. bleibt 0Fr.
