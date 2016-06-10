from django.core.management.base import BaseCommand
from .seed_bungalow import *
from .seed_bungalow_reservation import *

class Command(BaseCommand):
    help = 'This command will seed the all database'

    def handle(self, *args, **options):
        print('\n  Full Seeder is running...\n')

        print('    Deleting...')
        cleanBungalow()
        cleanBungalowReservation()

        print('    Inserting...')
        insertBungalow()
        insertBungalowReservation()