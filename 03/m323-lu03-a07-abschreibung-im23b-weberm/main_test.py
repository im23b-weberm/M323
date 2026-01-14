import main


def test_calculate_depreciation_normal_case():
    result = main.calculate_depreciation(1000, 0.1, 5)
    assert round(result, 2) == 590.49, f"Expected 590.49, got {result}"


def test_calculate_depreciation_zero_years():
    result = main.calculate_depreciation(1000, 0.1, 0)
    assert result == 1000, f"Expected 1000, got {result}"


def test_calculate_depreciation_zero_depreciation():
    result = main.calculate_depreciation(1000, 0.0, 5)
    assert result == 1000, f"Expected 1000, got {result}"


def test_calculate_depreciation_one_depreciation():
    result = main.calculate_depreciation(1000, 1.0, 5)
    assert result == 0, f"Expected 0, got {result}"


def test_calculate_depreciation_negative_initial_value():
    result = main.calculate_depreciation(-1000, 0.1, 5)
    assert round(result, 2) == -590.49, f"Expected -590.49, got {result}"


def test_calculate_depreciation_invalid_depreciation_rate_low():
    try:
        main.calculate_depreciation(1000, -0.1, 5)
    except ValueError as e:
        assert str(e) == "Der Abschreibungssatz muss zwischen 0 und 1 liegen."


def test_calculate_depreciation_invalid_depreciation_rate_high():
    try:
        main.calculate_depreciation(1000, 1.1, 5)
    except ValueError as e:
        assert str(e) == "Der Abschreibungssatz muss zwischen 0 und 1 liegen."


def test_calculate_depreciation_negative_years():
    try:
        main.calculate_depreciation(1000, 0.1, -1)
    except ValueError as e:
        assert str(e) == "Die Anzahl der Jahre kann nicht negativ sein."
