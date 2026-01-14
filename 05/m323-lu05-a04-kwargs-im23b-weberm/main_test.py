from main import user_profile


def test_user_profile_no_args():
    assert (
        user_profile() == ""
    ), "Should return an empty string when no keyword arguments are passed"


def test_user_profile_single_arg():
    assert (
        user_profile(name="Alice") == "Name: Alice"
    ), "Should return a formatted string for a single keyword argument"


def test_user_profile_multiple_args():
    assert (
        user_profile(name="Alice", age=30) == "Name: Alice, Age: 30"
    ), "Should return a formatted string for multiple keyword arguments"
