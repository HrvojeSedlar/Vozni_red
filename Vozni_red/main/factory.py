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
    broj = factory.Faker("randomize_nb_elements")
    vozac = factory.Iterator(Vozac.objects.all())

class StanicaFactory(DjangoModelFactory):
    class Meta:
        model = Stanica

    ime = factory.Faker("")
    adresa = factory.Faker("address")
    linije = factory.Faker("")

class LinijaFactory(DjangoModelFactory):
    class Meta:
        model = Linija

    ime = factory.Faker("")
    vrijeme_polaska = factory.Faker("")
    autobus = factory.Faker("")
    stanice = factory.Faker("")

class StanicaLinijaFactory(DjangoModelFactory):
    class Meta:
        model = StanicaLinija

    linija = factory.Faker("")
    stanica = factory.Faker("")
    OIB = factory.Faker("")