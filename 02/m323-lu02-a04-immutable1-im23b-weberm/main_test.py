import main


def test_students_is_list():
    """Test if 'students' is a list."""
    assert isinstance(
        main.students, list
    ), f'Expected a list, but got {type(main.students)}.'


def test_students_contains_tuples():
    """Test if 'students' contains only tuples."""
    for student in main.students:
        assert isinstance(student, tuple), f'Expected a tuple, but got {type(student)}.'


def test_students_tuple_structure():
    """Test the structure of the tuples in 'students'."""
    for student in main.students:
        assert len(student) == 3, f'Expected tuple of length 3, but got {len(student)}.'
        name, age, student_id = student
        assert isinstance(
            name, str
        ), f'Expected a string for name, but got {type(name)}.'
        assert isinstance(age, int), f'Expected an int for age, but got {type(age)}.'
        assert isinstance(
            student_id, int
        ), f'Expected an int for student_id, but got {type(student_id)}.'
