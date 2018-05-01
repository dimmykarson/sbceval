import csv
import os
module_dir = os.path.dirname(__file__)  # get current directory


def load_league(league_name):
    league = []
    file_path = os.path.join(module_dir, './docs/'+league_name+'.csv')
    pack_files = open(file_path, 'r')
    reader = csv.reader(pack_files, delimiter=';')
    for row in reader:
        league.append(row)
    return league

