from django.core.management.base import BaseCommand
from servicios.models import *

class Command(BaseCommand):
    help = 'This command will seed the database (Servicio)'

    def handle(self, *args, **options):
        print('\n  Servicio Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        ServicioType.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        sr1 = ServicioType(name= 'Canchas', description= "Todo espacio deportivo del club")
        sr1.save()
        sr1.servicio_set.create(name= "Alquiler 1 hora", price= 30)
        sr1.servicio_set.create(name= "Alquiler full day", price= 300)
        sr1.servicio_set.create(name= "Inscripcion equipo a torneo", price= 30)

        sr2 = ServicioType(name= 'Cine', description= "Uso del cine para proyeccion")
        sr2.save()
        sr2.servicio_set.create(name= "Entrada normal", price= 5)
        sr2.servicio_set.create(name= "Proyeccion personalizada", price= 100)
        sr2.servicio_set.create(name= "Precio por pareja", price= 8)

        sr3 = ServicioType(name= 'Otros', description= "Otros servicios")
        sr3.save()
        sr3.servicio_set.create(name= "Entrada piscina", price= 5)
        sr3.servicio_set.create(name= "Alquiler parrilla", price= 5)
        

        print('    Data has been inserted\n')