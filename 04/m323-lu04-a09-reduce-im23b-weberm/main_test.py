from main import factorial


def test_factorial():
    assert factorial(0) == 1  # Fakultät von 0 ist 1
    assert factorial(1) == 1  # Fakultät von 1 ist 1
    assert factorial(5) == 120  # Fakultät von 5 ist 5*4*3*2*1 = 120
    assert factorial(7) == 5040  # Fakultät von 7 ist 7*6*5*4*3*2*1 = 5040
    assert (
        factorial(10) == 3628800
    )  # Fakultät von 10 ist 10*9*8*7*6*5*4*3*2*1 = 3628800
