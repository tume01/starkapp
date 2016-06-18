from django.core.management.base import BaseCommand
from bungalow_reservation.models import BungalowReservation
from members.models import Member
import datetime


class Command(BaseCommand):
    help = 'This command will seed the database (BungalowReservation)'

    def handle(self, *args, **options):
        print('\n  Bungalow Seeder is running...\n')

        print('    Deleting...')
        cleanBungalowReservation()

        print('    Inserting...')
        insertBungalowReservation()


def cleanBungalowReservation():
    BungalowReservation.objects.all().delete()
    print('    BungalowReservations have been deleted')


def insertBungalowReservation():
    br1 = BungalowReservation()
    br1.arrival_date = datetime.date.today() + datetime.timedelta(days=-10)
    br1.departure_date = datetime.date.today() + datetime.timedelta(days=-1)
    asignRandomBungalow(br1)
    asignRandomMember(br1)
    br1.save()

    br1 = BungalowReservation()
    br1.arrival_date = datetime.date.today() + datetime.timedelta(days=25)
    br1.departure_date = datetime.date.today() + datetime.timedelta(days=31)
    asignRandomBungalow(br1)
    asignRandomMember(br1)
    br1.save()

    br1 = BungalowReservation()
    br1.arrival_date = datetime.date.today()
    br1.departure_date = datetime.date.today() + datetime.timedelta(days=7)
    asignRandomBungalow(br1)
    asignRandomMember(br1)
    br1.save()

    print('    BungalowReservations have been inserted')


import random
from bungalow.models import Bungalow

def asignRandomBungalow(br1):
    bungalows = Bungalow.objects.all()
    bungalow = random.choice(bungalows)

    br1.bungalow_number = bungalow.number
    br1.bungalow_type_id = bungalow.bungalow_type.id
    br1.bungalow_price = bungalow.bungalow_type.price
    br1.bungalow_capacity = bungalow.bungalow_type.capacity
    br1.bungalow_headquarter_name = bungalow.headquarter.name
    br1.bungalow_headquarter_id = bungalow.headquarter.id
    br1.bungalow_id = bungalow.id

def asignRandomMember(br1):
    members = Member.objects.all()
    member = random.choice(members)

    br1.member_id = member.id
    br1.member_membership_name = member.membership.membership_type.name
    br1.member_name = member.name
    br1.member_paternalLastName = member.paternalLastName
    br1.member_maternalLastName = member.maternalLastName
