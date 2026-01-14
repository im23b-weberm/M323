# your code for function average goes here
"""
average
"""
def average(list2):
    """
    :param list:
    :return:
    """
    if len(list2) > 0:
        return sum(list2)/len(list2)
    else:
        return 0

if __name__ == "__main__":
    list1 = [10, 20, 30, 40, 50]
    print(average(list1))
