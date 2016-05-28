from django.core.management.base import BaseCommand
from environment.models import *

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
        print('    Data has been deleted\n')

    def insertData(self):
        at1 = Environment(name='Ambiente 1', capacity=100, description='test', status=1)
        at1.save()

        print('    Data has been inserted\n')
