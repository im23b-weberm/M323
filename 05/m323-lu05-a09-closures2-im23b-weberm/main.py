"""
docstring
"""
# Version mit globaler Variable

# Ihr Ziel ist es, diesen Code zu refaktorieren,
# um die globale Variable durch ein Closure (create_counter) zu ersetzen.
def create_counter():
    # TODO: Implementieren Sie hier die Funktion create_counter
    counter = 0

    def increment_counter3():
        nonlocal counter
        counter += 1
        print(f"Counter: {counter}")
        return counter

    return increment_counter3


if __name__ == "__main__":
    # Auch mit dem Closure soll der Aufruf von increment_counter()
    # wie gewohnt funktionieren.
    # TODO: Erstellen Sie hier das Closure.
    increment_counter = create_counter()

    increment_counter()
    increment_counter()
    increment_counter()
