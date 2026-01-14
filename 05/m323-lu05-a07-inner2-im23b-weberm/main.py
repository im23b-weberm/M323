"""
abg sum
"""
def sum_and_average(numbers):
    """Find the sum and average of a list of numbers using inner functions.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        tuple: Sum and average of the numbers in the list.
    """
    # TODO: Innere Funktion zur Berechnung der Summe

    # TODO: Innere Funktion zur Berechnung des Durchschnitts

    # TODO: Rufen Sie die beiden inneren Funktionen auf und speichern Sie die Ergebnisse
    # TODO: Geben Sie die berechnete Summe und den Durchschnitt zurück
    def calculate_sum():
        return sum(numbers)  if numbers else 0
    def calculate_average():
        total = 0
        if numbers:
            for i in numbers:
                total += i
            return total/len(numbers)
        else:
            return 0
    return calculate_sum(), calculate_average()


if __name__ == '__main__':
    result = sum_and_average([1, 2, 3, 4, 5])
    print(result)  # Sollte (15, 3.0) zurückgeben
