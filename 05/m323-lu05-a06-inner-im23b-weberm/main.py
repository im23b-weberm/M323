"""
min/max
"""
def find_min_max(numbers2):
    """
    Find the minimum and maximum values in a list using inner functions.

    Parameters:
        numbers (list): List of numbers.

    Returns:
        tuple: Minimum and maximum values in the list.
    """
    # TODO: Innere Funktion zur Ermittlung des Minimums

    # TODO: Innere Funktion zur Ermittlung des Maximums

    # TODO: Rufen Sie die beiden inneren Funktionen auf und speichern Sie die Ergebnisse
    # TODO: Geben Sie das gefundene Minimum und Maximum zurück
    def find_min():
        return min(numbers2) if numbers2 else None
    def find_max():
        return max(numbers2)
    return find_min(), find_max() if numbers2 else None
if __name__ == '__main__':
    result = find_min_max([1, 2, 3, 4, 5])
    print(result)  # Sollte (1, 5) zurückgeben
