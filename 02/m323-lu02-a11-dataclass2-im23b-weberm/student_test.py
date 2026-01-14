from student import Student


def test_student_initialization():
    student = Student(name='John Doe')
    assert student.name == 'John Doe'
    assert student.grades == []
    assert student.graduated is False


def test_student_with_grades():
    student = Student(name='Jane Doe', grades=[85, 90, 78])
    assert student.name == 'Jane Doe'
    assert student.grades == [85, 90, 78]
    assert student.graduated is False


def test_student_grades_default_factory():
    student1 = Student(name='Student One')
    student2 = Student(name='Student Two')

    assert student1.grades == []  # Ensure both students start with an empty list
    assert student2.grades == []

    student1.grades.append(100)
    assert student1.grades == [100]  # Check if only student1's grades are modified
    assert student2.grades == []  # Ensure student2's grades remain unchanged

    student2.grades.append(95)
    assert student2.grades == [95]  # Check if only student2's grades are modified
    assert student1.grades == [100]  # Ensure student1's grades remain unchanged
