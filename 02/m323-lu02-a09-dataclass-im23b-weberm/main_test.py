import subprocess


def test_add_member():
    from team import Team
    from main import add_member

    team = Team(name='Team A')
    add_member(team, 'Alice')
    assert team.members == ['Alice']

    add_member(team, 'Bob')
    assert team.members == ['Alice', 'Bob']


def test_main_behavior():
    # Execute the main.py script and capture the output
    result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)

    # Expected output
    expected_output = "Team A Mitglieder: ['Alice']\n" "Team B Mitglieder: ['Bob']\n"

    assert result.stdout == expected_output
