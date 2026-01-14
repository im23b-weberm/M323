import pytest
from main import sort_students_by_grade


# Definieren Sie Fixtures für wiederkehrende Testdaten
@pytest.fixture
def sample_students():
    return [
        ('Alice', 4.0),
        ('Bob', 3.5),
        ('Charlie', 4.25),
        ('David', 5.5),
        ('Manuel', 3.75),
    ]


@pytest.fixture
def sample_students_with_same_grades():
    return [('Eve', 4.0), ('Frank', 4.0), ('Grace', 3.5)]


def test_sort_students_by_grade(sample_students):
    sorted_students = sort_students_by_grade(sample_students)

    assert sorted_students[0] == ('David', 5.5)
    assert sorted_students[1] == ('Charlie', 4.25)
    assert sorted_students[2] == ('Alice', 4.0)
    assert sorted_students[3] == ('Manuel', 3.75)
    assert sorted_students[4] == ('Bob', 3.5)


def test_empty_list():
    assert sort_students_by_grade([]) == []


def test_students_with_same_grades(sample_students_with_same_grades):
    sorted_students_same_grades = sort_students_by_grade(
        sample_students_with_same_grades
    )

    assert sorted_students_same_grades[0] == (
        'Eve',
        4.0,
    ) or sorted_students_same_grades[0] == (
        'Frank',
        4.0,
    )  # Reihenfolge von Eve und Frank kann variieren
    assert sorted_students_same_grades[2] == ('Grace', 3.5)
