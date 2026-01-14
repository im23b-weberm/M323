from main import find_min_max


def test_find_min_max_empty_list():
    assert find_min_max([]) == (
        None,
        None,
    ), "Should return (None, None) for an empty list"


def test_find_min_max_single_element():
    assert find_min_max([1]) == (
        1,
        1,
    ), "Should return (1, 1) for a list with a single element"


def test_find_min_max_multiple_elements():
    assert find_min_max([1, 2, 3, 4, 5]) == (
        1,
        5,
    ), "Should return (1, 5) for a list with multiple elements"


def test_find_min_max_negative_elements():
    assert find_min_max([-1, -2, -3, -4, -5]) == (
        -5,
        -1,
    ), "Should return (-5, -1) for a list with negative elements"


def test_find_min_max_mixed_elements():
    assert find_min_max([-1, 0, 1]) == (
        -1,
        1,
    ), "Should return (-1, 1) for a list with mixed elements"
