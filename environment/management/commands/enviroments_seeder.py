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
        at1 = Environment(name='Ambiente 1', capacity=100, description='test', status=1, headquarter_id = 1)
        at1.save()
        at1.environmentreservation_set.create(
            start_date = datetime.now(),
            end_date   = datetime.now() + timedelta(hours=9),
            price      = 100,
            status     = 0
        )
        at1.environmentreservation_set.create(
            start_date = datetime.now() - timedelta(hours=5),
            end_date   = datetime.now() + timedelta(hours=4),
            price      = 100,
            status     = 0
        )
        at1.environmentreservation_set.create(
            start_date = datetime.now(),
            end_date   = datetime.now() + timedelta(hours=15),
            price      = 100,
            status     = 0
        )

        at2 = Environment(name='Ambiente 2', capacity=100, description='test', status=1, headquarter_id = 1)
        at2.save()
        at2.environmentreservation_set.create(
            start_date = datetime.now(),
            end_date   = datetime.now() + timedelta(hours=9),
            price      = 100,
            status     = 0
        )
        at2.environmentreservation_set.create(
            start_date = datetime.now() - timedelta(hours=5),
            end_date   = datetime.now() + timedelta(hours=4),
            price      = 100,
            status     = 0
        )
        at2.environmentreservation_set.create(
            start_date = datetime.now(),
            end_date   = datetime.now() + timedelta(hours=15),
            price      = 100,
            status     = 0
        )

        print('    Data has been inserted\n')
