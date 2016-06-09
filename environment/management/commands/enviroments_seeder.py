from django.core.management.base import BaseCommand
from environment.models import *
from datetime import datetime

class Command(BaseCommand):
    help = 'This command will seed the database (Envoritoments)'

    def handle(self, *args, **options):
        print('\n  Environments Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        Environment.objects.all().delete()
        EnvironmentType.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        
        et1 = EnvironmentType(name='Campo de deporte', description='Canchas para jugar futbol', status=1)
        et1.save()
        et1.environment_set.create(name='Campo de Futbol 1', capacity=100, description='Pruebas ', status=1,reserved_date=datetime.now())
        et1.environment_set.create(name='Campo de Futbol 2', capacity=100, description='Pruebas ', status=1,reserved_date=datetime.now())
        et1.environment_set.create(name='Campo de Básquet 1', capacity=100, description='Pruebas ', status=1,reserved_date=datetime.now())
        et1.environment_set.create(name='Campo de Básquet 2', capacity=100, description='Pruebas ', status=1,reserved_date=datetime.now())
        et1.environment_set.create(name='Campo de Voley 1', capacity=100, description='Pruebas ', status=1,reserved_date=datetime.now())
        et1.environment_set.create(name='Campo de Voley 2', capacity=100, description='Pruebas ', status=1,reserved_date=datetime.now())
        

        print('    Data has been inserted\n')
