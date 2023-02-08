from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from main.models import Autobus, Linija, Stanica, Vozac

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

class VozacList(ListView):
    model = Vozac

class AutobusList(ListView):
    model = Autobus

class StanicaList(ListView):
    model = Stanica

class LinijaList(ListView):
    model = Linija

class VozacCreate(CreateView):
    model = Vozac
    fields = ['ime', 'prezime', 'OIB']

    def get_success_url(self):
        return reverse_lazy('main:vozaci')

class VozacUpdate(UpdateView):
    model = Vozac
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('main:vozaci')

class VozacDelete(DeleteView):
    model = Vozac

    def get_success_url(self):
        return reverse_lazy('main:vozaci')

class AutobusCreate(CreateView):
    model = Autobus
    fields = ['model', 'tablica', 'vozac']

    def get_success_url(self):
        return reverse_lazy('main:autobusi')

class AutobusUpdate(UpdateView):
    model = Autobus
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('main:autobusi')

class AutobusDelete(DeleteView):
    model = Autobus

    def get_success_url(self):
        return reverse_lazy('main:autobusi')

class StanicaCreate(CreateView):
    model = Stanica
    fields = ['ime', 'adresa', 'linije']

    def get_success_url(self):
        return reverse_lazy('main:stanice')

class StanicaUpdate(UpdateView):
    model = Stanica
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('main:stanice')

class StanicaDelete(DeleteView):
    model = Stanica

    def get_success_url(self):
        return reverse_lazy('main:stanice')

class LinijaCreate(CreateView):
    model = Linija
    fields = ['ime', 'vrijeme_polaska', 'autobus', 'stanice']

    def get_success_url(self):
        return reverse_lazy('main:linije')

class LinijaUpdate(UpdateView):
    model = Linija
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('main:linije')

class LinijaDelete(DeleteView):
    model = Linija

    def get_success_url(self):
        return reverse_lazy('main:linije')
