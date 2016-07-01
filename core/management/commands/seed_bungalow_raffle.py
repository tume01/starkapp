from django.core.management.base import BaseCommand
from bungalow_raffle.models import BungalowRaffle
from members.models import Member
import datetime


class Command(BaseCommand):
    help = 'This command will seed the database (BungalowReservation)'

    def handle(self, *args, **options):
        print('\n  Bungalow Raffle Seeder is running...\n')

        print('    Deleting...')
        cleanBungalowRaffle()

        print('    Inserting...')
        insertBungalowRaffle()


def cleanBungalowRaffle():
    BungalowRaffle.objects.all().delete()
    print('    BungalowRaffles have been deleted')


def insertBungalowRaffle():
    br1 = BungalowRaffle()
    br1.arrival_date = datetime.date.today() + datetime.timedelta(days=-10)
    asignRandomBungalow(br1)
    asignRandomMember(br1)
    br1.save()


    br1 = BungalowRaffle()
    br1.arrival_date = datetime.date.today() + datetime.timedelta(days=-2)
    asignRandomBungalow(br1)
    asignRandomMember(br1)
    br1.save()

    br1 = BungalowRaffle()
    br1.arrival_date = datetime.date.today() + datetime.timedelta(days=-7)
    asignRandomBungalow(br1)
    asignRandomMember(br1)
    br1.save()

    print('    BungalowRaffles have been inserted')


import random
from bungalow.models import Bungalow

def asignRandomBungalow(br1):
    bungalows = Bungalow.objects.all()
    bungalow = random.choice(bungalows)

    br1.bungalow_id = bungalow.id
    br1.bungalow_number = bungalow.number
    br1.bungalow_type_id = bungalow.bungalow_type.id
    br1.bungalow_type_name = bungalow.bungalow_type.name
    br1.bungalow_headquarter_id = bungalow.headquarter.id
    br1.bungalow_headquarter_name = bungalow.headquarter.name

def asignRandomMember(br1):
    members = Member.objects.all()
    member = random.choice(members)

    br1.member_id = member.id
    br1.member_membership_name = member.membership.membership_type.name
    br1.member_name = member.name
    br1.member_paternalLastName = member.paternalLastName
    br1.member_maternalLastName = member.maternalLastName
