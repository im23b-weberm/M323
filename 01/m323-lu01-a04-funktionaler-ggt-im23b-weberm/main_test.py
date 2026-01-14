import main


def test_ggt():
    assert main.ggt(56, 48) == 8
    assert main.ggt(101, 103) == 1
    assert main.ggt(60, 48) == 12
    assert main.ggt(0, 5) == 5
    assert main.ggt(5, 0) == 5
    assert main.ggt(0, 0) == 0
