"""
incrementing
"""
numbers1 = [1, 2, 3, 4, 5]


def increment_numbers(numbers):
    # Your code here
    """
    :param numbers:
    :return:
    """
    numberz = []
    for number in numbers:
        numberz.append(number + 1)
    return numberz


if __name__ == '__main__':
    print(numbers1)  # [1, 2, 3, 4, 5]
    print(increment_numbers(numbers1))  # [2, 3, 4, 5, 6]
    print(numbers1)  # [1, 2, 3, 4, 5]
