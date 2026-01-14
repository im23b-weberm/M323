from main import multiply_all


def test_multiply_all_no_args():
    assert multiply_all() == 1, "Should return 1 when no arguments are passed"


def test_multiply_all_single_arg():
    assert (
        multiply_all(3) == 3
    ), "Should return the same number when only one argument is passed"


def test_multiply_all_multiple_args():
    assert multiply_all(1, 2, 3, 4) == 24, "Should return the product of all arguments"


def test_multiply_all_with_zero():
    assert multiply_all(1, 2, 0, 4) == 0, "Should return 0 if any of the arguments is 0"
