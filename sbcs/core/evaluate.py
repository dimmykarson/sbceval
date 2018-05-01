from setuptools.command.easy_install import easy_install

from sbcs.core.packs import load_packs
from sbcs.core.league import load_league

margem = 1000
def evaluate_league(league_name):
    team_to_make = []
    packs = load_packs()
    league = load_league(league_name)
    total_gain = 0.0
    for team in league:
        if int(team[2])<0:
            continue
        pack = next((i for i in packs if int(i[0]) == int(team[2])), None)
        dif = (float(pack[2])-float(team[3]))
        if dif > margem:
            total_gain=total_gain+dif
            team_to_make.append([team, float(pack[2]), dif])
    return team_to_make

