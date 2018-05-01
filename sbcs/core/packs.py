import csv
import os
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, './docs/packs.csv')

def load_packs():
    packs = []
    pack_files = open(file_path, 'r')
    reader = csv.reader(pack_files, delimiter=';')
    for row in reader:
        packs.append(row)
    return packs