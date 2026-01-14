from student import Student
from main import add_grade, calculate_average, graduate_student
import subprocess


def test_add_grade():
    student = Student(name='John Doe')
    student = add_grade(student, 85)
    assert student.grades == [85]

    student = add_grade(student, 90)
    assert student.grades == [85, 90]


def test_calculate_average():
    student = Student(name='John Doe', grades=[85, 90, 75])
    average = calculate_average(student)
    assert average == 83.33

    student = Student(name='John Doe', grades=[])
    average = calculate_average(student)
    assert average == 0.0


def test_graduate_student():
    student = Student(name='John Doe', grades=[85, 90, 75])
    assert student.graduated is False

    student = graduate_student(student)
    assert student.graduated is True

    student = Student(name='Jane Doe', grades=[60, 65, 70])
    student = graduate_student(student)
    assert student.graduated is False


def test_integration():
    # Execute the main.py script and capture the output
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)

    # Expected output
    expected_output = (
        'Noten: [85, 75, 60]\n' 'Durchschnitt: 73.33\n' 'Absolviert: True\n'
    )

    assert result.stdout == expected_output
