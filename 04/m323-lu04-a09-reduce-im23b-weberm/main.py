"""
factorial
"""
from functools import reduce


def factorial(n):
    # Ihr Code hier
    if n == 0:
        return 1
    return reduce(lambda x, y: x*y, range(1, 1+n))


if __name__ == '__main__':
    result = factorial(5)
    print(result)  # Sollte 120 ausgeben
