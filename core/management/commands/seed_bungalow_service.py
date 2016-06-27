from django.core.management.base import BaseCommand
from bungalow_service.models import Bungalow_service
from bungalow_type.models import BungalowType

class Command(BaseCommand):
    help = 'This command will seed the database (Bungalow)'

    def handle(self, *args, **options):
        print('\n  Bungalow Seeder is running...\n')

        print('    Deleting...')
        cleanBungalow_service()

        print('    Inserting...')
        insertBungalow_service()

def cleanBungalow_service():
    BungalowType.objects.all().delete()
    print('    Bungalows Services have been deleted')

def insertBungalow_service():
    #bungalow services
    bs1 = Bungalow_service(name='Wi-Fi', description='', pay_per_hour=False, pay_per_day=False, pay_unique=True, price=100, deleted_at=None)
    bs1.save()

    bs2 = Bungalow_service(name='Cable', description='', pay_per_hour=False, pay_per_day=False, pay_unique=True, price=200, deleted_at=None)
    bs2.save()

    bs3 = Bungalow_service(name='Cable HD', description='', pay_per_hour=False, pay_per_day=False, pay_unique=True, price=250, deleted_at=None)
    bs3.save()

    list_service_1 = []
    list_service_1.append(bs1)

    list_service_2 = []
    list_service_2.append(bs1)
    list_service_2.append(bs2)

    list_service_3 = []
    list_service_3.append(bs1)
    list_service_3.append(bs2)
    list_service_3.append(bs3)
    
    
    bt1 = BungalowType(name= 'Small', price= 100, capacity= 2)
    bt1.save()
    bt1.bungalow_set.create(number= 101, status= 1, headquarter=getRandomHeadquarter() )
    bt1.bungalow_services = list_service_1
    bt1.save()

    bt2 = BungalowType(name= 'Medium', price= 180, capacity= 4)
    bt2.save()
    #bt2.bungalow_set.create(number= 201, status= 1, headquarter=getRandomHeadquarter() )
    bt2.bungalow_services = list_service_2
    bt2.save()

    bt3 = BungalowType(name= 'Large', price= 250, capacity= 8)
    bt3.save()
    #bt3.bungalow_set.create(number= 301, status= 1, headquarter=getRandomHeadquarter() )
    bt3.bungalow_services = list_service_3
    bt3.save()

    print('    Bungalows Services have been inserted')

import random
from headquarters.models import Headquarters

def getRandomHeadquarter():
    headquarters = Headquarters.objects.all()
    return random.choice(headquarters)