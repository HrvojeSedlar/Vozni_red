from django.contrib import admin

from main.models import Autobus, Linija, Stanica, StanicaLinija, Vozac

# Register your models here.

models_list = [Vozac, Autobus, Stanica, Linija, StanicaLinija]

admin.site.register(models_list)
