from django.core.management.base import BaseCommand
from headquarters.models import *

class Command(BaseCommand):
    help = 'This command will seed the database (Headquarters)'

    def handle(self, *args, **options):
        print('\n  Headquarters Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        Headquarters.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        at1 = Headquarters(name= 'Sede 1', location='ZONA SUR', description= 'test')
        at1.save()

        at1 = Headquarters(name= 'Sede 2', location='ZONA SUR', description= 'test')
        at1.save()

        at1 = Headquarters(name= 'Sede 3', location='ZONA SUR', description= 'test')
        at1.save()

        at1 = Headquarters(name= 'Sede 4', location='ZONA SUR', description= 'test')
        at1.save()

        at1 = Headquarters(name= 'Sede 5', location='ZONA SUR', description= 'test')
        at1.save()

        at1 = Headquarters(name= 'Sede 6', location='ZONA SUR', description= 'test')
        at1.save()
        
        print('    Data has been inserted\n')