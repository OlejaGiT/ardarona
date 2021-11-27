from typing import Any, Tuple
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import *


def index(request):
    home = Home.objects.all()
    team = Team.objects.all()
    pril = PrilTeam.objects.all()
    context = {"team": team, "pril": pril, "home": home}
    return render(request, "main/index.html", context=context)
