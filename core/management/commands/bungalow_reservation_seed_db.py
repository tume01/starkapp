from django.core.management.base import BaseCommand
from bungalow_reservation.models import BungalowReservation
import datetime

class Command(BaseCommand):
    help = 'This command will seed the database (BungalowReservation)'

    def handle(self, *args, **options):
        print('\n  Bungalow Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        BungalowReservation.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        br1 = BungalowReservation(price= 300)
        br1.arrival_date =  datetime.date.today()
        br1.departure_date =  datetime.date.today() + datetime.timedelta(days=7)
        br1.save()

        br1 = BungalowReservation(price= 300)
        br1.arrival_date =  datetime.date.today()
        br1.departure_date =  datetime.date.today() + datetime.timedelta(days=7)
        br1.save()
        
        br1 = BungalowReservation(price= 300)
        br1.arrival_date =  datetime.date.today()
        br1.departure_date =  datetime.date.today() + datetime.timedelta(days=7)
        br1.save()

        print('    Data has been inserted\n')
