from main import absolute_value


def test_absolute_value():
    assert absolute_value(-5.5) == 5.5
    assert absolute_value(0) == 0
    assert absolute_value(3.14) == 3.14
    assert absolute_value(-0) == 0  # Testen von -0
    assert absolute_value(10.1) == 10.1
    assert absolute_value(-10.1) == 10.1
    assert absolute_value(1) == 1
    assert absolute_value(-1) == 1
