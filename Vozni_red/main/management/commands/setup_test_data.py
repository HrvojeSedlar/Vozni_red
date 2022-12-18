import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Vozac, Autobus, Stanica, Linija, StanicaLinija
from main.factory import (
    VozacFactory,
    AutobusFactory,
    StanicaFactory,
    LinijaFactory,
    StanicaLinijaFactory,
)

NUM_VOZACS = 50
NUM_AUTOBUSS = 50
NUM_STANICAS = 100
NUM_LINIJAS = 30
NUM_STANICALINIJAS = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Vozac, Autobus, Stanica, Linija, StanicaLinija]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_VOZACS):
            vozac = VozacFactory()

        for _ in range(NUM_AUTOBUSS):
            autobus = AutobusFactory()

        for _ in range(NUM_STANICAS):
            stanica = StanicaFactory()

        for _ in range(NUM_LINIJAS):
            linija = LinijaFactory()

        for _ in range(NUM_STANICALINIJAS):
            stanicalinija = StanicaLinijaFactory()