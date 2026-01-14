# test_team.py
from team import Team


def test_team_initialization():
    team = Team(name='Team A')
    assert team.name == 'Team A'
    assert team.members == []


def test_team_with_members():
    team = Team(name='Team B', members=['Alice', 'Bob'])
    assert team.name == 'Team B'
    assert team.members == ['Alice', 'Bob']
