import main


def test_recursive_sum():
    assert main.recursive_sum([5, 3, 9, 1, 7]) == 25
    assert main.recursive_sum([1, 1, 1, 1, 1, 1]) == 6
    assert main.recursive_sum([100]) == 100
    assert main.recursive_sum([]) == 0
    assert main.recursive_sum([-5, 5, -5, 5]) == 0
