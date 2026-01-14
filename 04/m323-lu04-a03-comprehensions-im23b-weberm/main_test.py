from main import squares_of_even_numbers


def test_squares_of_even_numbers():
    result = squares_of_even_numbers()
    assert len(result) == 50  # Es gibt 50 gerade Zahlen von 1 bis 100
    assert result[0] == 4  # Das Quadrat von 2 ist 4
    assert result[-1] == 10000  # Das Quadrat von 100 ist 10000
    for i in result:
        # Überprüfen, ob alle Zahlen in der Ergebnisliste Quadrate von geraden Zahlen sind
        assert int(i**0.5) % 2 == 0
