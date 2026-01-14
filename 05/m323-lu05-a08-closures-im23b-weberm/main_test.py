from main import create_multiplier


def test_create_multiplier():
    multiply_by_two = create_multiplier(2)
    assert multiply_by_two(3) == 6, "Fehler beim Multiplizieren mit 2"

    multiply_by_five = create_multiplier(5)
    assert multiply_by_five(4) == 20, "Fehler beim Multiplizieren mit 5"

    multiply_by_zero = create_multiplier(0)
    assert multiply_by_zero(100) == 0, "Fehler beim Multiplizieren mit 0"

    print("Alle Testfälle bestanden!")
