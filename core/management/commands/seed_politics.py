from django.core.management.base import BaseCommand
from politics.models import *

class Command(BaseCommand):
    help = 'This command will seed the database (Politics)'

    def handle(self, *args, **options):
        print('\n  Politics Seeder is running...\n')

        print('    Deleting...')
        cleanPolitics()

        print('    Inserting...')
        insertPolitic()

def cleanPolitics():
        Politic.objects.all().delete()
        print('    Politics data has been deleted\n')

def insertPolitic():
        p1 = Politic(name= 'MAX_DAYS_DELETE_EVENT', value=14)
        p1.save()

        p2 = Politic(name= 'DAYS_OBJECTION_PERIOD', value=14)
        p2.save()

        p3 = Politic(name= 'MONTHS_MEMBERSHIP_PAYMENT_PERIOD', value=12)
        p3.save()

        p4 = Politic(name= 'MAX_AGE_MALE_AFFILIATE', value=18)
        p4.save()

        p5 = Politic(name= 'MAX_AGE_FEMALE_AFFILIATE', value=21)
        p5.save()

        
        print('    Politics data has been inserted\n')
