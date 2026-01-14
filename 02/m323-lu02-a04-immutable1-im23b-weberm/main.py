"""
students
"""
students = [
    ('Hari', 20, 1),
    ('Theo', 19, 2),
    ('Anthony', 18, 3)
]


def print_students(student_list):
    """
    :param student_list:
    :return:
    """
    # Your code here

    for student in student_list:
        name, age, idz = student
        print(f'Name: {name}, Alter: {age}, ID: {idz}')


if __name__ == '__main__':
    print_students(students)
