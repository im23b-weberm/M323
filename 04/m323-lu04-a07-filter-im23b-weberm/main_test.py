from main import filter_even_numbers


def test_filter_even_numbers():
    assert filter_even_numbers(list(range(1, 51))) == list(
        range(2, 51, 2)
    )  # Testen von 1 bis 50
    assert filter_even_numbers([]) == []  # Testen einer leeren Liste
    assert filter_even_numbers([1, 3, 5, 7]) == []  # Liste ohne gerade Zahlen
    assert filter_even_numbers([2, 4, 6, 8]) == [
        2,
        4,
        6,
        8,
    ]  # Liste nur mit geraden Zahlen
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [2, 4]  # Gemischte Liste
