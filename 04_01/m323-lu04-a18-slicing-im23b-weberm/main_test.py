from main import slicing_special_cases


def test_slicing_special_cases():
    result = slicing_special_cases()

    assert result["first_three"] == [1, 2, 3], "Fehler bei den ersten drei Elementen"
    assert result["last_two"] == [4, 5], "Fehler bei den letzten zwei Elementen"
    assert result["reversed_lst"] == [5, 4, 3, 2, 1], "Fehler beim Umkehren der Liste"
    assert result["every_second"] == [1, 3, 5], "Fehler bei jedem zweiten Element"
    assert result["between_neg4_and_neg1"] == [
        2,
        3,
        4,
    ], "Fehler zwischen den Indizes -4 und -1"
    assert result["first_three_reversed"] == [
        3,
        2,
        1,
    ], "Fehler bei den ersten drei umgekehrten Elementen"
    assert result["last_two_reversed"] == [
        5,
        4,
    ], "Fehler bei den letzten zwei umgekehrten Elementen"
    assert result["reversed_every_second"] == [
        5,
        3,
        1,
    ], "Fehler bei jedem zweiten Element der umgekehrten Liste"
    assert result["between_neg4_and_neg1_reversed_every_second"] == [
        4,
        2,
    ], "Fehler bei der Verkettung von Slicing-Operationen"
