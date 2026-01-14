from main import get_user_by_id


users = [
    {'id': 1, 'name': 'Alice'},
    {'id': 2, 'name': 'Bob'},
    {'id': 3, 'name': 'Charlie'},
    {'id': 4, 'name': 'David'},
]


def test_existing_id():
    result = get_user_by_id(users, 3)
    assert result == {
        'id': 3,
        'name': 'Charlie',
    }, f"Erwartet: {{'id': 3, 'name': 'Charlie'}}, Erhalten: {result}"


def test_non_existing_id():
    result = get_user_by_id(users, 5)
    assert result is None, f'Erwartet: None, Erhalten: {result}'


def test_first_id():
    result = get_user_by_id(users, 1)
    assert result == {
        'id': 1,
        'name': 'Alice',
    }, f"Erwartet: {{'id': 1, 'name': 'Alice'}}, Erhalten: {result}"


def test_last_id():
    result = get_user_by_id(users, 4)
    assert result == {
        'id': 4,
        'name': 'David',
    }, f"Erwartet: {{'id': 4, 'name': 'David'}}, Erhalten: {result}"
