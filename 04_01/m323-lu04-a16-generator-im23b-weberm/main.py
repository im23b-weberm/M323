"""
numberz
"""
def even_numbers_generator(m):
    """
    Generiert alle geraden Zahlen bis zum Wert m.

    Ein gerader Wert ist eine ganze Zahl, die ohne Rest durch 2 teilbar ist.

    :param m: Der maximale Wert, bis zu dem gerade Zahlen generiert werden sollen.
    :return: Ein Generator für gerade Zahlen.
    """
    for num1 in range(1, m + 1):
        if num1% 2 == 0:
            yield num1


if __name__ == '__main__':
    # Testen Sie Ihren Generator
    for num in even_numbers_generator(15):
        print(num)
