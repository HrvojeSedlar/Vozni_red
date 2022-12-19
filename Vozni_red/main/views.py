from django.shortcuts import render
from django.views.generic import ListView
from main.models import Vozac, Autobus, Stanica, Linija, StanicaLinija

# Create your views here.

def index(request):
    return render(request, 'index.html')

class VozacList(ListView):
    model = Vozac

class AutobusList(ListView):
    model = Autobus

class StanicaList(ListView):
    model = Stanica

class LinijaList(ListView):
    model = Linija
