"""
filterkaffee
"""
def filter_by_age(students3, age):
    """
    Filtert die Studentenliste nach einem gegebenen Mindestalter.

    :param students: Liste von Studentendaten
    :param age: Mindestalter für den Filter
    :return: Gefilterte Liste von Studenten
    """
    result = []
    for student in students3:
        if student['age'] >= age:
            result.append(student)
    return result


def filter_by_class(students1, class_name):
    """
    Filtert die Studentenliste nach einer gegebenen Klasse.

    :param students: Liste von Studentendaten
    :param class_name: Klassenname für den Filter
    :return: Gefilterte Liste von Studenten
    """
    result = []
    for student in students1:
        if student['class'] == class_name:
            result.append(student)
    return result


def filter_students(students2, filter_function, *args):
    """
    Filtert die Studentenliste mit einer gegebenen Filterfunktion.

    :param students: Liste von Studentendaten
    :param filter_function: Funktion, die zum Filtern der Studenten verwendet wird
    :param args: Zusätzliche Argumente für die Filterfunktion
    :return: Gefilterte Liste von Studenten
    """
    # your code here
    return filter_function(students2, *args)


if __name__ == '__main__':
    students = [
        {'name': 'Alice', 'age': 15, 'class': '10A'},
        {'name': 'Bob', 'age': 16, 'class': '10B'},
        {'name': 'Charlie', 'age': 14, 'class': '9A'},
    ]
    # your code here
