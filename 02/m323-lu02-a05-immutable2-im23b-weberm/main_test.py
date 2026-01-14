import main


def test_increment_positive_numbers():
    """Test the function with a list of positive numbers."""
    input_list = [1, 2, 3, 4, 5]
    expected_output = [2, 3, 4, 5, 6]
    assert main.increment_numbers(input_list) == expected_output


def test_increment_negative_numbers():
    """Test the function with a list of negative numbers."""
    input_list = [-1, -2, -3, -4, -5]
    expected_output = [0, -1, -2, -3, -4]
    assert main.increment_numbers(input_list) == expected_output


def test_increment_mixed_numbers():
    """Test the function with a list of mixed positive and negative numbers."""
    input_list = [-1, 0, 1, 2, -2]
    expected_output = [0, 1, 2, 3, -1]
    assert main.increment_numbers(input_list) == expected_output


def test_increment_empty_list():
    """Test the function with an empty list."""
    input_list = []
    expected_output = []
    assert main.increment_numbers(input_list) == expected_output


def test_original_list_unchanged():
    """Test that the original list remains unchanged."""
    input_list = [1, 2, 3]
    original_list = input_list.copy()
    main.increment_numbers(input_list)
    assert (
        input_list == original_list
    ), f'Expected the original list to remain unchanged, but got {input_list}.'
