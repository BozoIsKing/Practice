from random import choice
from math import ceil


def make_groups(list_teams, num_groups):
    groups = []
    for n in range(num_groups):
        groups.append([])

    for i in range(ceil(len(list_teams) / num_groups)):
        for group in groups:
            if len(list_teams) == 0:
                break
            team_sel = choice(list_teams)
            group.append(team_sel)
            list_teams.remove(team_sel)

    return groups

