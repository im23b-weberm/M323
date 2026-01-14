"""
banana
"""
def to_uppercase(words2):
    """
    Convert each word in the list to uppercase using the map function.
    Args:
    - words (list): List of words to be converted to uppercase.

    Returns:
    - list: List of words in uppercase.
    """
    # Your code here
    uppercase_list2 = list(map(str.upper, words2))
    return uppercase_list2


if __name__ == '__main__':
    words = ['apple', 'banana', 'cherry']
    uppercase_list = to_uppercase(words)
    print(uppercase_list)
