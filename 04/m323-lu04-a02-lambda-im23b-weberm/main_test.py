from main import circle_area, square_area, rectangle_area


def test_circle_area():
    assert abs(circle_area(5) - 78.5398163397) < 1e-10


def test_square_area():
    assert square_area(4) == 16


def test_rectangle_area():
    assert rectangle_area(3, 5) == 15
