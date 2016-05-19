from django.core.management.base import BaseCommand
from bungalows.models import *

class Command(BaseCommand):
    help = 'This command will seed the database (Bungalow)'

    def handle(self, *args, **options):
        print('\n  Bungalow Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        BungalowType.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        bt1 = BungalowType(name= 'Small', price= 100, capacity= 2)
        bt1.save()
        bt1.bungalow_set.create(number= 101, status= 1)
        bt1.bungalow_set.create(number= 102, status= 1)
        bt1.bungalow_set.create(number= 103, status= 1)

        bt2 = BungalowType(name= 'Medium', price= 180, capacity= 4)
        bt2.save()
        bt2.bungalow_set.create(number= 201, status= 1)
        bt2.bungalow_set.create(number= 202, status= 1)
        bt2.bungalow_set.create(number= 203, status= 1)

        bt3 = BungalowType(name= 'Large', price= 250, capacity= 8)
        bt3.save()
        bt3.bungalow_set.create(number= 301, status= 1)
        bt3.bungalow_set.create(number= 302, status= 1)
        bt3.bungalow_set.create(number= 303, status= 1)

        print('    Data has been inserted\n')
