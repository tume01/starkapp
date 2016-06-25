from django.core.management.base import BaseCommand
from events_type.models import *
from events.models import *
from datetime import datetime,timedelta
import random

def cleanEventType():
    EventsType.objects.all().delete()
    print('    Data has been deleted\n')

def insertEventType():
    sr1 = EventsType(name= 'Privado', description= "Estos eventos son solo para los miembros del club", status=0)
    sr1.save()

    sr2 = EventsType(name= 'Fiesta', description= "Estos eventos son para todos los presentes en el club", status = 0)
    sr2.save()

    sr3 = EventsType(name= 'Concierto', description= "Estos eventos son conciertos", status = 0)
    sr3.save()

    sr4 = EventsType(name= 'Exposicion', description= "Estos eventos son involucrados al arte", status = 0)
    sr4.save()

    sr5 = EventsType(name= 'Nocturno', description= "Estos eventos son involucrados al arte", status = 0)
    sr5.save()

    sr6 = EventsType(name= 'Cultural', description= "Estos eventos son involucrados al arte", status = 0)
    sr6.save()

    event = Event(event_type=sr1, description="Evento Corporacion Razer", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr1, description="Evento de Aventura", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr2, description="Fiesta del Pacifico", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr2, description="Fiesta Rumba", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr3, description="Concierto Coldplay", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr3, description="Concierto Gorillaz", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr4, description="Exposicion PUCP", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr4, description="Exposicion ACM", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr5, description="Maraton Nocturna", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr5, description="Maraton Peliculas de Terror", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr6, description="Yoga", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr6, description="Evento Cultural Japones", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='url', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    print('Data has been inserted\n')

def getMember():
    return Member.objects.first()

def getRandomHeadquarter():
    headquarters = Headquarters.objects.all()
    return random.choice(headquarters)