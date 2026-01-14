from main import create_counter


def test_create_counter():
    counter = create_counter()
    assert counter() == 1
    assert counter() == 2
    assert counter() == 3
