from main import even_numbers_generator


def test_even_numbers_generator():
    even_numbers = list(even_numbers_generator(15))
    assert even_numbers == [2, 4, 6, 8, 10, 12, 14]
