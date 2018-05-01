from sbcs.core.evaluate import evaluate_league
from scipy.optimize import linprog
import numpy as np
leagues = ["bundesliga", "calcioa", "hyundai", "proleague", "premier", "laliga",
           "meiji_yasuda", "mls", "dawry_jameel", "ligue1", "efl", "eredivisie",
           "liganos", "russian", "liganos", "bancomer", "superlig"]

#own = ['311', '287', '290', '291', '300', '301', '302', '145', '166', '178', '181']

def optimize_coins(max_coins, own):
    c = []
    a = []
    b = []
    mapping = []
    for league in leagues:
        evs = evaluate_league(league)
        a_aux = []
        for ev in evs:
           cod = ev[0][0]
           if cod in own:
               continue
           c.append(-1*ev[2])
           a_aux.append(float(ev[0][3]))
           mapping.append(ev)
        a = a+a_aux
    a = [a]
    inteira = [1]*len(c)
    a.append(inteira)
    b.append(float(max_coins))
    b.append(len(c))
    bounds = [(0,1)]*len(c)
    res = linprog(c, A_ub=a, b_ub=b, bounds=bounds, options={"disp": True})
    z = np.array(res.x)
    to_produce = []
    total = 0.0
    ganho_total = 0.0
    for i in range(len(z)):
        if z[i] == 1:
            to_produce.append(mapping[i])
            total=total+float(mapping[i][0][3])
            ganho_total = ganho_total+float(mapping[i][1])
    lucro = ganho_total-total
    return to_produce, total, ganho_total, lucro
