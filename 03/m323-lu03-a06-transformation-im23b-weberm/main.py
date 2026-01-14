"""
emploee
"""
def transform_employee_data(employees, transformation_function, *args):
    return transformation_function(employees, *args)


def increase_salary_by_department(employees, department, percentage):
    for employee in employees:
        if employee['department'] == department:
            employee['salary'] += employee['salary'] * percentage / 100
    return employees


def convert_names_to_uppercase(employees):
    for employee in employees:
        employee['name'] = employee['name'].upper()
    return employees


def filter_by_age(employees, age, comparison='greater'):
    result = []
    for employee in employees:
        if comparison == 'greater' and employee['age'] > age:
            result.append(employee)
        elif comparison == 'less' and employee['age'] < age:
            result.append(employee)
    return result


if __name__ == '__main__':
    pass
