import countries_data


def test_sort_countries_by_name():
    sample_data = [{'name': 'B'}, {'name': 'A'}, {'name': 'C'}]
    assert countries_data.sort_countries_by_name(sample_data) == [
        {'name': 'A'},
        {'name': 'B'},
        {'name': 'C'},
    ]


def test_sort_countries_by_capital():
    sample_data = [{'capital': 'B'}, {'capital': 'A'}, {'capital': 'C'}]
    assert countries_data.sort_countries_by_capital(sample_data) == [
        {'capital': 'A'},
        {'capital': 'B'},
        {'capital': 'C'},
    ]


def test_sort_countries_by_population():
    sample_data = [{'population': 2}, {'population': 1}, {'population': 3}]
    assert countries_data.sort_countries_by_population(sample_data) == [
        {'population': 3},
        {'population': 2},
        {'population': 1},
    ]


def test_get_most_spoken_languages():
    sample_data = [
        {'languages': ['A', 'B']},
        {'languages': ['A', 'C']},
        {'languages': ['A', 'B']},
    ]
    assert countries_data.get_ten_most_spoken_languages(sample_data) == [
        ('A', 3),
        ('B', 2),
        ('C', 1),
    ]


def test_get_most_populated_countries():
    sample_data = [
        {'name': 'A', 'population': 2},
        {'name': 'B', 'population': 1},
        {'name': 'C', 'population': 3},
    ]
    assert countries_data.get_ten_most_populated_countries(sample_data) == [
        ('C', 3),
        ('A', 2),
        ('B', 1),
    ]
