from django.core.management.base import BaseCommand
from headquarters.models import Headquarters

class Command(BaseCommand):
    help = 'This command will seed the database (Headquarter)'

    def handle(self, *args, **options):
        print('\n  Headquarter Seeder is running...\n')

        print('    Deleting...')
        cleanHeadquarter()

        print('    Inserting...')
        insertHeadquarter()


def cleanHeadquarter():
    Headquarters.objects.all().delete()
    print('    Headquarters have been deleted')

def insertHeadquarter():
    Headquarters(name= "Chosica", description="club campestre", location="").save()
    Headquarters(name= "Playa", description="club de playa", location="").save()

    print('    Headquarters have been inserted')