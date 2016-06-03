from django.core.management.base import BaseCommand
from events_type.models import *

class Command(BaseCommand):
    help = 'This command will seed the database (Events types)'

    def handle(self, *args, **options):
        print('\n  Events types Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        EventsType.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        sr1 = EventsType(name= 'Privado', description= "Estos eventos son solo para los miembros del club", status=1)
        sr1.save()

        sr2 = EventsType(name= 'Público', description= "Estos eventos son para todos los presentes en el club", status = 1)
        sr2.save()

        print('Data has been inserted\n')