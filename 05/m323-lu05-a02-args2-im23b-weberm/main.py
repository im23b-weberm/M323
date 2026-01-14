"""
reverse
"""
def reverse_merge(*args):
    """
    Merges multiple lists and returns the merged list in reversed order.

    Parameters:
        *args (list): Variable number of lists to be merged.

    Returns:
        list: The merged list in reversed order.
    """
    # TODO: Implementiere die Funktion
    fin_list = []
    for i in args:
        fin_list.extend(i)
    return fin_list[::-1]

if __name__ == '__main__':
    # Teste deine Funktion
    print(
        reverse_merge([1, 2], [3, 4], [5, 6])
    )  # Erwarteter Output: [6, 5, 4, 3, 2, 1]
