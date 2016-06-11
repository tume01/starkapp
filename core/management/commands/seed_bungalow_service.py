from django.core.management.base import BaseCommand
from bungalow_service.models import Bungalow_service
from bungalow_type.models import BungalowType

class Command(BaseCommand):
    help = 'This command will seed the database (Bungalow)'

    def handle(self, *args, **options):
        print('\n  Bungalow Seeder is running...\n')

        #print('    Deleting...')
        #cleanBungalow_service()

        #print('    Inserting...')
        #insertBungalow_service()

def cleanBungalow_service():
    BungalowType.objects.all().delete()
    print('    Bungalows Services have been deleted')

def insertBungalow_service():
    bt1 = BungalowType(name= 'Small', price= 100, capacity= 2)
    bt1.save()
    bt1.bungalow_set.create(number= 101, status= 1, headquarter=getRandomHeadquarter() )

    bt2 = BungalowType(name= 'Medium', price= 180, capacity= 4)
    bt2.save()
    #bt2.bungalow_set.create(number= 201, status= 1, headquarter=getRandomHeadquarter() )

    bt3 = BungalowType(name= 'Large', price= 250, capacity= 8)
    bt3.save()
    #bt3.bungalow_set.create(number= 301, status= 1, headquarter=getRandomHeadquarter() )

    print('    Bungalows Services have been inserted')

import random
from headquarters.models import Headquarters

def getRandomHeadquarter():
    headquarters = Headquarters.objects.all()
    return random.choice(headquarters)