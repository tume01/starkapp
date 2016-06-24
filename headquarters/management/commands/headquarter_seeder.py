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
        print('    Headquarters data has been deleted\n')

    def insertData(self):
        hq1 = Headquarters(name= 'Lima HQ', location='Av. Javier Prado Este 159', description= 'Sede Principal', status= 1, ubigeos_id = 1295)
        hq1.save()

        hq2 = Headquarters(name= 'Arequipa Club', location='Calle Yanahuara 143', description= 'Sede Arequipa', status= 1, ubigeos_id=357)
        hq2.save()
        
        print('    Data has been inserted\n')
