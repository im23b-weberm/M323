"""
student
"""
from student import Student
def add_grade(student2, grade):
    """
    Returns a new Student instance with the added grade.
    """
    # todo: implement this function
    new_grades = student2.grades + [grade]
    return Student(name=student2.name, grades=new_grades, graduated=student2.graduated)


def calculate_average(student3):
    """
    Returns the average of the student's grades.
    """
    # todo: implement this function
    if not student3.grades:
        return 0.0
    return round(sum(student3.grades) / len(student3.grades), 2)


def graduate_student(student4):
    """
    Graduates the student if the average grade is 70 or above.
    """
    # todo: implement this function
    average1 = calculate_average(student4)
    if average1 >= 70:
        return Student(name=student4.name, grades=student4.grades, graduated=True)
    return student4


if __name__ == '__main__':
    student = Student(name='John Doe')
    student = add_grade(student, 85)
    student = add_grade(student, 75)
    student = add_grade(student, 60)

    print(f'Noten: {student.grades}')
    average = calculate_average(student)
    print(f'Durchschnitt: {average}')

    student = graduate_student(student)
    print(f'Absolviert: {student.graduated}')
