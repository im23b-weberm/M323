from main import to_uppercase


def test_to_uppercase():
    assert to_uppercase(['apple', 'banana', 'cherry']) == ['APPLE', 'BANANA', 'CHERRY']
    assert to_uppercase([]) == []  # Testen einer leeren Liste
    assert to_uppercase(['Hello', 'World']) == ['HELLO', 'WORLD']
    assert to_uppercase(['test', 'TEST', 'TeSt']) == [
        'TEST',
        'TEST',
        'TEST',
    ]  # Testen von gemischten Groß- und Kleinschreibungen
