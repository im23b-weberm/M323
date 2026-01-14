"""
team2
"""
from team import Team
def add_member(team, member):
    """
    Adds a new member to the team's members list.
    """
    # todo
    team.members.append(member)


if __name__ == '__main__':
    team1 = Team(name='Team A')
    team2 = Team(name='Team B')

    add_member(team1, 'Alice')
    add_member(team2, 'Bob')

    print(
        f'{team1.name} Mitglieder: {team1.members}'
    )  # Output: Team A Mitglieder: ['Alice']
    print(
        f'{team2.name} Mitglieder: {team2.members}'
    )  # Output: Team B Mitglieder: ['Bob']
