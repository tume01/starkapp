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

    event = Event(event_type=sr1, name="Evento Corporacion Razer",description="Evento destinado para GAMERS", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event1.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr1,name="Evento de Aventura", description="Evento para los aventureros", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event1.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr2, name="Fiesta del Pacifico",description="Aquí la pasarás bien con tus amigos", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event2.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr2, name="Fiesta Rumba",description="Ven y diviertete con amigos y familia", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event2.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr3, name="Concierto Coldplay",description="Ven canta tus canciones favoritas de Coldplay", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event3.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr3, name="Concierto Gorillaz",description="Ven canta tus canciones favoritas de Gorillaz", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event3.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr4, name="Exposicion PUCP",description="No te pierdas la exposición de docentes de la PUCP", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event4.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr4, name="Exposicion ACM",description="No te despiertas un nuevo camino en la informática", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event4.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr5, name="Maraton Nocturna",description="Sal a correr con tu familia", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event5.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr5, name="Maraton Peliculas de Terror",description="Ven y disfruta de los clásicos del cine de terror", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event5.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr6, name="Yoga",description="Practica yoga para relajarte del día a día", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event6.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    event = Event(event_type=sr6, name="Evento Cultural Japones",description="Aprende un poco más de la cultura japonesa", start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9), assistance=10, price_member=10, price_invited=12, status=0, photo='events/event6.jpg', creator=getMember(), headquarter=getRandomHeadquarter())
    event.save()

    print('Data has been inserted\n')

def getMember():
    return Member.objects.first()

def getRandomHeadquarter():
    headquarters = Headquarters.objects.all()
    return random.choice(headquarters)
