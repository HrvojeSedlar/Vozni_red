from django.db import models

# Create your models here.

class Vozac(models.Model):
    ime = models.CharField(max_length=30)
    prezime = models.CharField(max_length=30)
    OIB = models.DecimalField(max_digits=11, decimal_places=0, primary_key=True)

    def __str__(self):
        return f"{self.ime}"


class Autobus(models.Model):
    model = models.CharField(max_length=30)
    tablica = models.CharField(max_length=8, default=1, primary_key=True)
    vozac = models.OneToOneField(Vozac, on_delete=models.CASCADE) #One to One

    def __str__(self):
        return f"{self.tablica}"


class Stanica(models.Model):
    ime = models.CharField(max_length=30, primary_key=True)
    adresa = models.CharField(max_length=60)
    linije = models.ManyToManyField("Linija", through="StanicaLinija") #Many to Many

    def __str__(self):
        return f"{self.ime}"

class Linija(models.Model):
    ime = models.CharField(max_length=30, primary_key=True)
    vrijeme_polaska = models.TimeField(auto_now=False, auto_now_add=False)
    autobus = models.ForeignKey(Autobus, on_delete=models.CASCADE) #One to Many
    stanice = models.ManyToManyField(Stanica, through="StanicaLinija") #Many to Many

    def __str__(self):
        return f"{self.ime}"

class StanicaLinija(models.Model):
    linija = models.ForeignKey(Linija, on_delete=models.CASCADE) #One to Many
    stanica = models.ForeignKey(Stanica, on_delete=models.CASCADE) #One to Many

    #def __str__(self):
    #    return self.stanica
