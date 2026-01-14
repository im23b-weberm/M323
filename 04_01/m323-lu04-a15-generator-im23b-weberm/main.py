"""
yieald
"""
def fibonacci_generator(n):
    """
    Generiert die Fibonacci-Sequenz bis zum n-ten Wert.

    Die Fibonacci-Sequenz ist eine Reihe von Zahlen, bei der jede Zahl
    die Summe der beiden vorhergehenden Zahlen ist. Die Sequenz beginnt mit 0 und 1.
    Beispiel: 0, 1, 1, 2, 3, 5, 8, 13, ...

    :param n: Die Anzahl der zu generierenden Fibonacci-Zahlen.
    :return: Ein Generator für die Fibonacci-Sequenz.
    """
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # Testen Sie Ihren Generator
    for num in fibonacci_generator(10):
        print(num)
