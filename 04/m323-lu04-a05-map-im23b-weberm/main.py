"""
dubble
"""
def double_elements(numbers2):
    """
    Double each element in the list using the map function.
    Args:
    - numbers (list): List of numbers to be doubled.
    Returns:
    - list: List of doubled numbers.
    """
    # TODO: Your code here
    newlist = list(map(lambda x: 2*x, numbers2))
    return newlist


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    doubled_list = double_elements(numbers)
    print(doubled_list)
