from django.core.management.base import BaseCommand
from identity_document_type.models import *

class Command(BaseCommand):
    help = 'This command will seed the database (Identity Document types)'

    def handle(self, *args, **options):
        print('\n  Identity document types Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        Identity_Document_Type.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        doc1 = Identity_Document_Type(name= 'DNI', descripcion= 'Documento nacional de identidad', status=1)
        doc1.save()

        doc2 = Identity_Document_Type(name= 'Pasaporte', descripcion= 'Documento que permite viajar a otros paises', status = 1)
        doc2.save()

        print('Data has been inserted\n')