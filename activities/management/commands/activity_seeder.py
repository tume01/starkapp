from activities.models import *
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'This command will seed the database (Bungalow)'

    def handle(self, *args, **options):
        print('\n  Activity Type Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        Activity.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=4, name='Activity 1', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=4, name='Activity 2', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=4, name='Activity 3', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=4, name='Activity 4', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=4, name='Activity 5', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=4, name='Activity 6', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=5, name='Activity 7', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=5, name='Activity 8', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=5, name='Activity 9', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=5, name='Activity 10', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=6, name='Activity 11', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=6, name='Activity 12', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=6, name='Activity 13', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=6, name='Activity 14', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()

        at1 = Activity(deleted_at=None, price=100, enviroment_id=22, activity_type_id=6, name='Activity 15', 
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
        at1.save()
        
        print('    Data has been inserted\n')