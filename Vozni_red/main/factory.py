import factory
from factory.django import DjangoModelFactory

from main.models import *

class VozacFactory(DjangoModelFactory):
    class Meta:
        model = Vozac

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    OIB = factory.Faker("random_number", digits=11, fix_len=True)

class AutobusFactory(DjangoModelFactory):
    class Meta:
        model = Autobus

    model = factory.Faker("name")
    tablica = factory.Faker("license_plate")
    vozac = factory.Iterator(Vozac.objects.all())

class StanicaFactory(DjangoModelFactory):
    class Meta:
        model = Stanica

    ime = factory.Faker("text", max_nb_chars=15)
    adresa = factory.Faker("address")

class LinijaFactory(DjangoModelFactory):
    class Meta:
        model = Linija

    ime = factory.Faker("sentence", nb_words=3)
    vrijeme_polaska = factory.Faker("time")
    autobus = factory.Iterator(Autobus.objects.all())

class StanicaLinijaFactory(DjangoModelFactory):
    class Meta:
        model = StanicaLinija

    linija = factory.Iterator(Linija.objects.all())
    stanica = factory.Iterator(Stanica.objects.all())