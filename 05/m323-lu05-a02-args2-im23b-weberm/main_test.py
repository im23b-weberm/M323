from main import reverse_merge


def test_reverse_merge_no_args():
    assert (
        reverse_merge() == []
    ), "Should return an empty list when no arguments are passed"


def test_reverse_merge_single_list():
    assert reverse_merge([1, 2, 3]) == [
        3,
        2,
        1,
    ], "Should return the reversed list when only one list is passed"


def test_reverse_merge_multiple_lists():
    assert reverse_merge([1, 2], [3, 4], [5, 6]) == [
        6,
        5,
        4,
        3,
        2,
        1,
    ], "Should return the merged list in reversed order"


def test_reverse_merge_with_empty_lists():
    assert reverse_merge([], [1, 2], []) == [
        2,
        1,
    ], "Should ignore empty lists and return the merged list in reversed order"
