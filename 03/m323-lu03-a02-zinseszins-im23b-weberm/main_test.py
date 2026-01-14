import main


def test_compound_interest():
    # Test mit einem Anfangsbetrag von 1000, 5% Zinssatz und einer Laufzeit von 5 Jahren
    assert round(main.compound_interest(1000, 0.05, 5), 2) == 1276.28

    # Test mit einem Anfangsbetrag von 2000, 3% Zinssatz und einer Laufzeit von 10 Jahren
    assert round(main.compound_interest(2000, 0.03, 10), 2) == 2687.83

    # Test mit einem Anfangsbetrag von 5000, 7% Zinssatz und einer Laufzeit von 0 Jahren
    assert round(main.compound_interest(5000, 0.07, 0), 2) == 5000.00

    # Test mit einem Anfangsbetrag von 0, 5% Zinssatz und einer Laufzeit von 5 Jahren
    assert round(main.compound_interest(0, 0.05, 5), 2) == 0.00

    # Test mit einem Anfangsbetrag von 1000, 0% Zinssatz und einer Laufzeit von 5 Jahren
    assert round(main.compound_interest(1000, 0, 5), 2) == 1000.00


def test_compound_interest_edge_cases():
    # Test mit einem negativen Anfangsbetrag
    assert round(main.compound_interest(-1000, 0.05, 5), 2) == -1276.28

    # Test mit einem negativen Zinssatz (z.B. bei einer Strafgebühr)
    assert round(main.compound_interest(1000, -0.05, 5), 2) == 773.78

    # Test mit negativer Laufzeit (sollte in der Realität nicht vorkommen, aber gut für die Funktion zu handhaben)
    try:
        main.compound_interest(1000, 0.05, -5)
    except ValueError as e:
        assert str(e) == "Die Laufzeit kann nicht negativ sein."

    # Test mit einem Zinssatz von mehr als 100% (also 1.0)
    assert round(main.compound_interest(1000, 2, 2), 2) == 9000.00

    # Test mit einer sehr hohen Laufzeit
    assert round(main.compound_interest(1000, 0.01, 500), 2) == 144772.77

    # Test mit einem sehr niedrigen Zinssatz
    assert round(main.compound_interest(1000, 0.000001, 500), 4) == 1000.5001
