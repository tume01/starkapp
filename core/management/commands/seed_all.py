from django.core.management.base import BaseCommand
from .seed_bungalow import *
from .seed_bungalow_reservation import *
from .seed_headquarter import *
from .seed_environments import *
from .seed_login import Command as LoginSeed

class Command(BaseCommand):
    help = 'This command will seed the all database'

    def handle(self, *args, **options):
        print('\n  Full Seeder is running...\n')

        print('    Deleting...')
        login = LoginSeed() 
        login.cleanLogin()
        cleanHeadquarter()
        cleanEnvironments()
        cleanBungalow()
        cleanBungalowReservation()

        print('\n    Inserting...')
        login.insertLogin()
        insertHeadquarter()
        insertEnvironments()
        insertBungalow()
        insertBungalowReservation()
