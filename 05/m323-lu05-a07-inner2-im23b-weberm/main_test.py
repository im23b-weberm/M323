from main import sum_and_average


def test_sum_and_average_empty_list():
    assert sum_and_average([]) == (0, 0), "Should return (0, 0) for an empty list"


def test_sum_and_average_single_element():
    assert sum_and_average([1]) == (
        1,
        1,
    ), "Should return (1, 1) for a list with a single element"


def test_sum_and_average_multiple_elements():
    assert sum_and_average([1, 2, 3, 4, 5]) == (
        15,
        3.0,
    ), "Should return (15, 3.0) for a list with multiple elements"


def test_sum_and_average_negative_elements():
    assert sum_and_average([-1, -2, -3, -4, -5]) == (
        -15,
        -3.0,
    ), "Should return (-15, -3.0) for a list with negative elements"


def test_sum_and_average_mixed_elements():
    assert sum_and_average([-1, 0, 1]) == (
        0,
        0,
    ), "Should return (0, 0) for a list with mixed elements"
