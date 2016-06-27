from django.core.management.base import BaseCommand
from activity_types.models import *
from activities.models import *
from environment.models import *
from datetime import datetime,timedelta


def cleanActivity():
    ActivityType.objects.all().delete()
    Activity.objects.all().delete()
    print('    Data has been deleted\n')

def insertActivity():

    at1 = ActivityType(name= 'Aire Libre', price= 100, description= 'Actividades realizadas al aire libre en ambientes abiertos')
    at1.save()

    at2 = ActivityType(name= 'Cultural', price= 300, description= 'Actividades culturales')
    at2.save()

    at3 = ActivityType(name= 'Fiesta', price= 300, description= 'Actividades de fiesta')
    at3.save()

    at4 = ActivityType(name= 'Gastronomica', price= 300, description= 'Actividades gastronomicas')
    at4.save()

    at5 = ActivityType(name= 'Musical', price= 300, description= 'Actividades musicales')
    at5.save()


    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at1, name='Exposicion de Cometas',
                        attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at1, name='Show de globos Aeroestaticos',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at1, name='Busqueda del Tesoro de Verano',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at1, name='Muestra de Pinturas del Curso de Arte',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at1, name='Exposicion botonica',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at2, name='Exposicion de pinturas Curso de Arte 1',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at2, name='Exposicion Curso de Origami',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at2, name='Exposicion Curso de Pintura con las manos',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at3, name='Fiesta Fin de Verano',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at3, name='Fiesta Fin de Finales',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at3, name='Fiesta Aniversario Club',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at4, name='Misturita Verano',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at5, name='Concierto curso de violin 1',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at5, name='Concierto Curso de piano 1',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()

    a1 = Activity(deleted_at=None, price=100, enviroment=getFirstEnviroment(), activity_type=at5, name='Concierto Curso de bonda 1',
                    attendance=10, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=9))
    a1.save()


    print('    Data has been inserted\n')

def getFirstEnviroment():
    return Environment.objects.first()