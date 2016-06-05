from django.core.management.base import BaseCommand
from bungalow.models import Bungalow
from bungalow_type.models import BungalowType

class Command(BaseCommand):
    help = 'This command will seed the database (Bungalow)'

    def handle(self, *args, **options):
        print('\n  Bungalow Seeder is running...\n')

        print('    Deleting...')
        cleanBungalow()

        print('    Inserting...')
        insertBungalow()

def cleanBungalow():
    BungalowType.objects.all().delete()
    print('    Bungalows have been deleted')

def insertBungalow():
    bt1 = BungalowType(name= 'Small', price= 100, capacity= 2)
    bt1.save()
    bt1.bungalow_set.create(number= 101, status= 1)
    bt1.bungalow_set.create(number= 102, status= 1)
    bt1.bungalow_set.create(number= 103, status= 1)
    bt1.bungalow_set.create(number= 104, status= 1)
    bt1.bungalow_set.create(number= 105, status= 1)
    bt1.bungalow_set.create(number= 106, status= 1)
    bt1.bungalow_set.create(number= 107, status= 1)
    bt1.bungalow_set.create(number= 108, status= 1)

    bt2 = BungalowType(name= 'Medium', price= 180, capacity= 4)
    bt2.save()
    bt2.bungalow_set.create(number= 201, status= 1)
    bt2.bungalow_set.create(number= 202, status= 1)
    bt2.bungalow_set.create(number= 203, status= 1)
    bt2.bungalow_set.create(number= 204, status= 1)
    bt2.bungalow_set.create(number= 205, status= 1)
    bt2.bungalow_set.create(number= 206, status= 1)
    bt2.bungalow_set.create(number= 207, status= 1)
    bt2.bungalow_set.create(number= 208, status= 1)

    bt3 = BungalowType(name= 'Large', price= 250, capacity= 8)
    bt3.save()
    bt3.bungalow_set.create(number= 301, status= 1)
    bt3.bungalow_set.create(number= 302, status= 1)
    bt3.bungalow_set.create(number= 303, status= 1)
    bt3.bungalow_set.create(number= 304, status= 1)
    bt3.bungalow_set.create(number= 305, status= 1)
    bt3.bungalow_set.create(number= 306, status= 1)
    bt3.bungalow_set.create(number= 307, status= 1)
    bt3.bungalow_set.create(number= 308, status= 1)
    bt3.bungalow_set.create(number= 303, status= 1)

    print('    Bungalows have been inserted')
