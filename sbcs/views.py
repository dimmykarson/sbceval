from django.shortcuts import render, render_to_response
from sbcs.core.optimize import leagues
from sbcs.core.league import load_league
from sbcs.core.optimize import optimize_coins
from django.contrib import messages
from sbcs.core.update_estimatives import update
from sbcs.models import *
from sbcs.core.packs import load_packs
import json

def privacidade(request):
    return render(request, 'geral/privacidade.html', {})

def termos(request):
    return render(request, 'geral/termos.html', {})

def index(request):
    #salvarBanco();
    tuples = load_leagues()
    sbc_feitos = None
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        sbc_feitos = [obj.as_dict() for obj in SBC_FEITOS.objects.filter(user=user).all()]
    context={'leagues':tuples, 'value':0, 'sbc_feitos':json.dumps({"data": sbc_feitos})}
    return render(request, 'sbcs/index.html', context)

def salvarBanco():
    Pack.objects.all().delete()
    SBC.objects.all().delete()

    tuples = load_leagues()
    packs = load_packs()
    for p in packs:
        pack = Pack()
        pack.cod = p[0]
        pack.name = p[1]
        pack.cost = float(p[2])
        pack.cost_points = float(p[3])
        pack.save()
    #126;Vancouver Whitecaps;-1;9150.0;6900.0;6850.0

    for t in tuples:
        print(t)
        for l in t[1]:
            sbc = SBC()
            sbc.liga = t[0]
            sbc.cod = l[0]
            sbc.team = l[1]
            if(int(l[2])>0):
                sbc.pack = Pack.objects.get(cod=int(l[2]))
                sbc.valido = True
            else:
                sbc.valido=False
            sbc.preco_ps4 = float(l[3])
            sbc.preco_xone = float(l[4])
            sbc.preco_pc = float(l[5])
            sbc.save()


def evaluate(request):
    checked = request.POST.getlist('team')
    try:
        value = request.POST.get('value')
    except:
        value = "0"
    try:
        platform = request.POST.get('platform')
    except:
        platform = "3"
    platform = int(platform)
    result = optimize_coins(value, checked, platform)
    if len(result[0])==0:
        messages.info(request, "With this coins, we can do nothing :( ")
        return index(request)
    else:
        if platform == 3:
            platform_n = 'PC'
        elif platform == 4:
            platform_n = 'Playstation 4'
        else:
            platform_n = 'Xbox One'
        context={'to_produce':result[0], 'total_cost':result[1], 'total_gain':result[2], 'lucro':result[3], 'platform_n':platform_n, 'platform':platform}
        logar_usuario(request, checked)
        return render(request, 'sbcs/result.html', context)

def logar_usuario(request, checked):
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        if not user:
            return
        SBC_FEITOS.objects.filter(user=user).delete()
        for z in checked:
            sbc_f = SBC_FEITOS()
            sbc = SBC.objects.filter(id=z).get()
            if not sbc:
                continue
            sbc_f.sbc = sbc
            sbc_f.user = user
            sbc_f.save()




def up(request):
    update()
    tuples = load_leagues()
    context = {'leagues': tuples, 'value': 0}
    return render(request, 'sbcs/index.html', context)

def load_leagues():
    tuples = []
    ls = load_macro_sbc()
    for league in ls:
        tuples.append([league+"", SBC.objects.filter(liga=league)])
    return tuples

def load_macro_sbc():
   s = SBC.objects.order_by('liga').values('liga').distinct()
   l = [x.get('liga') for x in s]
   return l