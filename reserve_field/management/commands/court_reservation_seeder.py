from django.core.management.base import BaseCommand
from reserve_field.models import *

class Command(BaseCommand):
    help = 'This command will seed the database (Events types)'

    def handle(self, *args, **options):
        print('\n  Events types Seeder is running...\n')

        print('    Deleting...')    
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        FieldReservation.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        sr1 = FieldReservation(headquarter_id= 1, court_name='Pichanga',court_headquarter_name='Sede 1',court_type=0,user_id=2,member_membership_name='Exclusivo',
            member_name='Christian',member_paternalLastName='Bedon',member_maternalLastName='Villalobos',reservation_hour="20:00",reservation_duration=2,
            reservation_date="2016-06-20",status=1)
        sr1.save()

        print('Data has been inserted\n')
