"""
calc
"""
add = lambda a, b: a + b# Ihr Code hier

subtract = lambda a, b: a - b  # Ihr Code hier

multiply = lambda a, b: a * b  # Ihr Code hier

divide = lambda a, b: a / b if b != 0 else 'Division durch Null ist nicht erlaubt!'

if __name__ == '__main__':

    print (add(5, 10))
    print(subtract(10, 5))
    print(multiply(3, 4))
    print(divide(15, 3))
