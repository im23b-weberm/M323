"""
find user
"""
def get_user_by_id(user_list, user_id):
    """
    Gibt das Benutzer-Dictionary zurück, das der angegebenen ID entspricht.
    Verwenden Sie eine Generator-Expression und die Funktion next().

    Args:
    - user_id (int): Die ID des gesuchten Benutzers.
    - user_list (list): Die Liste der Benutzer-Dictionarys.

    Returns:
    - dict: Das Dictionary des Benutzers mit der angegebenen ID. Wenn kein Benutzer gefunden wird, gibt die Funktion
    None zurück.
    """
    return next((user for user in user_list if user['id'] == user_id), None)


if __name__ == '__main__':
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'},
        {'id': 4, 'name': 'David'},
    ]

    # Testen Sie get_user_by_id
    print(get_user_by_id(users, 3))
