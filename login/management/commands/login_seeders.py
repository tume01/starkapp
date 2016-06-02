from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = 'This command will seed the database (Users and types)'

    def handle(self, *args, **options):
        print('\n  Users Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        User.objects.all().delete()
        Group.objects.all().delete()
        print('    Data has been deleted\n')

    def insertData(self):
        user1 = User.objects.create_user(username='usuario', password='1111')
        user2 = User.objects.create_user(username='administrador', password='1111')
        user3 = User.objects.create_user(username='bungalow', password='1111')
        user4 = User.objects.create_user(username='evento', password='1111')
        user5 = User.objects.create_user(username='cancha', password='1111')
        user6 = User.objects.create_user(username='cajero', password='1111')
        user7 = User.objects.create_user(username='membresia', password='1111')
        user8 = User.objects.create_user(username='empresa', password='1111')

        usuario = Group.objects.create(name='usuarios')
        admin = Group.objects.create(name='admins')
        bungalows = Group.objects.create(name='bungalows')
        eventos = Group.objects.create(name='eventos')
        canchas = Group.objects.create(name='canchas')
        cajero = Group.objects.create(name='cajeros')
        membresia = Group.objects.create(name='membresias')
        empresa = Group.objects.create(name='empresas')

        usuario.user_set.add(user1)
        admin.user_set.add(user2)
        bungalows.user_set.add(user3)
        eventos.user_set.add(user4)
        canchas.user_set.add(user5)
        cajero.user_set.add(user6)
        membresia.user_set.add(user7)
        empresa.user_set.add(user8)



        print('Data has been inserted\n')