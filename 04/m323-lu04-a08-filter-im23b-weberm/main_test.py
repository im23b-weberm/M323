from main import filter_long_words


def test_filter_long_words():
    assert filter_long_words(['apple', 'banana', 'cherry', 'date']) == [
        'banana',
        'cherry',
    ]
    assert filter_long_words([]) == []  # Testen einer leeren Liste
    assert filter_long_words(['short', 'even shorter', 'shortest']) == [
        'even shorter',
        'shortest',
    ]
    assert filter_long_words(['apple', 'date']) == []
    assert filter_long_words(['pineapple', 'strawberry', 'kiwi']) == [
        'pineapple',
        'strawberry',
    ]
