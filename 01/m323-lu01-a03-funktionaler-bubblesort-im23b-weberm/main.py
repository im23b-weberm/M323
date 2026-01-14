"""
functional sort
"""
def bubble_pass(numbrs):
    """

    :param numbrs:
    :return:
    """
    if len(numbrs) <= 1:
        return numbrs
    if numbrs[0] > numbrs[1]:
        return [numbrs[1]] + bubble_pass([numbrs[0]] + numbrs[2:])
    return [numbrs[0]] + bubble_pass(numbrs[1:])
def sort(numbers, length=None):
    """

    :param numbers:
    :return:
    """
    if length is None:
        length = len(numbers)
    if length == 1:
        return numbers
    numbers = bubble_pass(numbers)
    return sort(numbers, length - 1)

if __name__ == '__main__':
    number = [64, 34, 25, 12, 22, 11, 90]
    sort(number)
    print(number)
