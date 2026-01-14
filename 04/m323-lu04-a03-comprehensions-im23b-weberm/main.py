"""
squarepants
"""
def squares_of_even_numbers():
    # TODO: Erstelle eine Liste der Quadrate aller geraden Zahlen von 1 bis 100
    return [x ** 2 for x in range(1, 101) if x % 2 == 0]


if __name__ == '__main__':
    result = squares_of_even_numbers()
    print(result)
