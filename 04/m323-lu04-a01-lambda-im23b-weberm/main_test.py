from main import add, subtract, multiply, divide


def test_add():
    assert add(5, 10) == 15
    assert add(0, 0) == 0
    assert add(-5, 5) == 0


def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
    assert subtract(-5, 5) == -10


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-3, 4) == -12


def test_divide():
    assert divide(15, 3) == 5
    assert divide(0, 5) == 0
    assert divide(15, 0) == "Division durch Null ist nicht erlaubt!"
