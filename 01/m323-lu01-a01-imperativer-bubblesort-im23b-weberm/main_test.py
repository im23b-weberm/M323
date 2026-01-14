import main


def test_sort_presorted():
    # Testfall 1: Testen einer bereits sortierten Liste
    numbers = [11, 22, 34, 45, 64, 90]
    main.sort(numbers)
    assert numbers == [11, 22, 34, 45, 64, 90], "Testfall 1 fehlgeschlagen"


def test_sort_inverse():
    # Testfall 2: Testen einer umgekehrt sortierten Liste
    numbers = [90, 64, 45, 34, 22, 11]
    main.sort(numbers)
    assert numbers == [11, 22, 34, 45, 64, 90], "Testfall 2 fehlgeschlagen"
