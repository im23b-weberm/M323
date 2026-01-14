"""
list sorting
"""
def sort(numbers):
    """
    :param numbers:
    :return:
    """
    length = len(numbers)

    for i in range(length):
        for j in range(0, length - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]




if __name__ == '__main__':
    number = [64, 34, 25, 12, 22, 11, 90]
    sort(number)
    print(number)
