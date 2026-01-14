from main import count_calls


def test_count_calls(capsys):
    # Zähler zurücksetzen
    counter = 0

    @count_calls
    def function():
        nonlocal counter
        counter += 1

    # Erster Aufruf der Funktion
    function()
    captured = capsys.readouterr()
    assert captured.out == "Die Funktion function wurde 1 mal aufgerufen.\n"
    assert counter == 1

    # Zweiter Aufruf der Funktion
    function()
    captured = capsys.readouterr()
    assert captured.out == "Die Funktion function wurde 2 mal aufgerufen.\n"
    assert counter == 2
