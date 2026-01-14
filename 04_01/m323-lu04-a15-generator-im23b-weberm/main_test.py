from main import fibonacci_generator


def test_fibonacci_generator():
    fib_sequence = list(fibonacci_generator(10))
    assert fib_sequence == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
