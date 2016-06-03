from django.core.management.base import BaseCommand
from activity_types.models import *

class Command(BaseCommand):
    help = 'This command will seed the database (Bungalow)'

    def handle(self, *args, **options):
        print('\n  Activity Type Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        ActivityType.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        at1 = ActivityType(name= 'Pequena', price= 100, description= 'test')
        at1.save()

        at1 = ActivityType(name= 'Mediana', price= 200, description= 'test')
        at1.save()

        at1 = ActivityType(name= 'Grande', price= 300, description= 'test')
        at1.save()
        
        print('    Data has been inserted\n')
