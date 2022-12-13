from django.db import models

# Create your models here.

class Vozac(models.Model):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    OIB = models.CharField(max_length=11)

    def __str__(self):
        return self.name


class Autobus(models.Model):
    marka = models.CharField(max_length=30)
    linijski_broj = models.CharField(max_length=30)
    vozac = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Linija(models.Model):
    vrijeme_polaska = models.CharField(max_length=30)
    autobus = models.CharField(max_length=30)
    odrediste = models.CharField(max_length=30)

    def __str__(self):
        return self.name