"""
sum rum
"""
def recursive_sum(numbers):
    """
    This function calculates the sum of a list of numbers recursively.

    :param numbers: List of numbers
    :return: Sum of numbers
    """
    # TODO: Implement the recursive function to calculate the sum of numbers

    if len(numbers) == 0:
        return 0

    return numbers[0] + recursive_sum(numbers[1:])

if __name__ == '__main__':
    number = [5, 3, 9, 1, 7]
    result = recursive_sum(number)
    print('The sum of numbers is:', result)
