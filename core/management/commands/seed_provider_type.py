from django.core.management.base import BaseCommand
#from product_types.models import *
from products.models import *
from providers.models import *
from datetime import datetime,timedelta

class Command(BaseCommand):
    help = 'This command will seed the database (Provider Types)'

    def handle(self, *args, **options):
        print('\n  Provider Types Seeder is running...\n')

        print('    Deleting...')
        cleanProviderTypes()

        print('    Inserting...')
        insertProviderTypes()

def cleanProviderTypes():
    ProviderType.objects.all().delete()
    print('    Data has been deleted\n')

def insertProviderTypes():
    prt1 = ProviderType(name= 'Proveedor', description= 'Proveedor de productos en general.')
    prt1.save()

    prt2 = ProviderType(name= 'Concesionario', description= 'Proveedor de servicios  alimenticios.')
    prt2.save()

    print('    Data has been inserted\n')