from main import filter_students_by_grade


def test_filter_students_by_grade():
    students = [
        ('Alice', 4.0),
        ('Bob', 3.5),
        ('Charlie', 4.25),
        ('David', 5.5),
        ('Manuel', 3.75),
    ]
    result = filter_students_by_grade(students)

    # Überprüfen, ob nur die Studenten mit Noten kleiner als 4.0 zurückgegeben werden
    assert len(result) == 2
    assert result[0] == ('Bob', 3.5)
    assert result[1] == ('Manuel', 3.75)
