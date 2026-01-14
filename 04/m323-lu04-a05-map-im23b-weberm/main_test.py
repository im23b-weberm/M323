from main import double_elements


def test_double_elements():
    assert double_elements([1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
    assert double_elements([]) == []  # Testing an empty list
    assert double_elements([-1, -2, -3]) == [-2, -4, -6]  # Testing negative numbers
    assert double_elements([0, 0, 0]) == [0, 0, 0]  # Testing zeros
