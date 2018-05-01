from django.shortcuts import render, render_to_response
from sbcs.core.optimize import leagues
from sbcs.core.league import load_league
from sbcs.core.optimize import optimize_coins
from django.contrib import messages

def index(request):
    tuples = load_leagues()
    context={'leagues':tuples, 'value':0}
    return render(request, 'sbcs/index.html', context)

def evaluate(request):
    checked = request.POST.getlist('team')
    try:
        value = request.POST.get('value')
    except:
        value = "0"
    result = optimize_coins(value, checked)
    if len(result[0])==0:
        messages.info(request, "With this coins, we can do nothing :( ")
        return index(request)
    else:
        context={'to_produce':result[0], 'total_cost':result[1], 'total_gain':result[2], 'lucro':result[3]}
        return render(request, 'sbcs/result.html', context)

def load_leagues():
    tuples = []
    for league in leagues:
        l = load_league(league)
        tuples.append([league, l])
    return tuples