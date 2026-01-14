import main


def test_average_positive_numbers():
    """Test the function with a list of positive numbers."""
    input_list = [10, 20, 30, 40, 50]
    expected_output = 30.0
    assert main.average(input_list) == expected_output


def test_average_negative_numbers():
    """Test the function with a list of negative numbers."""
    input_list = [-10, -20, -30, -40, -50]
    expected_output = -30.0
    assert main.average(input_list) == expected_output


def test_average_mixed_numbers():
    """Test the function with a list of mixed positive and negative numbers."""
    input_list = [-10, 20, -30, 40, -50]
    expected_output = -6.0
    assert main.average(input_list) == expected_output


def test_average_empty_list():
    """Test the function with an empty list."""
    input_list = []
    expected_output = 0.0  # Or None, depending on your implementation
    assert main.average(input_list) == expected_output


def test_average_single_element():
    """Test the function with a single-element list."""
    input_list = [42]
    expected_output = 42.0
    assert main.average(input_list) == expected_output
