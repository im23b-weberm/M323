from main import check_permission, User


def test_check_permission(capsys):
    # Erstellen von Benutzerobjekten
    alice = User("Alice", 3)
    bob = User("Bob", 1)

    @check_permission(2)
    def test_view_profile(user):
        print(f"{user.username} kann das Profil anzeigen.")

    @check_permission(4)
    def test_edit_profile(user):
        print(f"{user.username} kann das Profil bearbeiten.")

    # Test für Alice, die das Profil anzeigen kann
    test_view_profile(alice)
    captured = capsys.readouterr()
    assert captured.out == "Alice kann das Profil anzeigen.\n"

    # Test für Alice, die das Profil nicht bearbeiten kann
    test_edit_profile(alice)
    captured = capsys.readouterr()
    assert captured.out == "Alice hat nicht genügend Berechtigungen.\n"

    # Test für Bob, der das Profil nicht anzeigen kann
    test_view_profile(bob)
    captured = capsys.readouterr()
    assert captured.out == "Bob hat nicht genügend Berechtigungen.\n"

    # Test für Bob, der das Profil nicht bearbeiten kann
    test_edit_profile(bob)
    captured = capsys.readouterr()
    assert captured.out == "Bob hat nicht genügend Berechtigungen.\n"
