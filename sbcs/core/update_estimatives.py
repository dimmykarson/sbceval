import requests
from bs4 import BeautifulSoup

def update_leagues(league):
    page = requests.get("https://www.futbin.com/squad-building-challenges/LEAGUES/"+str(league))
    soup = BeautifulSoup(page.content, 'html.parser')
    boxes = soup.find_all('div', class_='main_chal_box')
    prices_estimed = []
    for box in boxes:
        team1 = BeautifulSoup("<html>"+str(box)+"</html>", "html.parser")
        team_name = team1.find_all('div', class_='chal_name')
        name_ = team_name[0].string.strip()
        estimed = team1.find('div', class_='est_chal_prices_holder').attrs
        pc = estimed['data-pc-price']
        ps = estimed['data-ps-price']
        xone = estimed['data-xone-price']
        prices_estimed.append([name_, float(pc), float(ps), float(xone)])
    return prices_estimed

leagues = [["bundesliga",303], ["calcioa",226], ["hyundai",449], ["proleague",447], ["premier",446], ["laliga",448],
           ["meiji_yasuda",304], ["mls",227], ["dawry_jameel",135], ["ligue1",134], ["efl",63], ["eredivisie",62],
           ["liganos",39], ["russian",40], ["bancomer",12], ["superlig",11]]

from sbcs.core.league import load_league
import csv
import os
module_dir = os.path.dirname(__file__)  # get current directory



def update():
    for l_tuple in leagues:
        name = l_tuple[0]
        print(name)
        estimeted=update_leagues(l_tuple[1])
        league = load_league(name)
        for e in estimeted:
            n = e[0].strip()
            for item in league:
                if item[1]==n:
                    item[3]= e[1]
                    try:
                        item[4] = e[2]
                        item[5] = e[3]
                    except:
                        item.append(e[2])
                        item.append(e[3])
        file_path = os.path.join(module_dir, './docs/'+name+'.csv')
        file = open(file_path, 'w', encoding="UTF-8")
        file.seek(0)
        file.truncate()
        for l in league:
            file.write(str(l[0])+";"+l[1]+";"+str(l[2])+";"+str(l[3])+";"+str(l[4])+";"+str(l[5])+"\n")


