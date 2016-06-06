from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from datetime import datetime, timedelta
from identity_document_type.models import *
from memberships.models import *
from membership_application.models import *
from members.models import *
from fine.models import *
from promotions.models import *



class Command(BaseCommand):
    help = 'This command will seed the database (Users and types)'

    def handle(self, *args, **options):
        print('\n  Users Seeder is running...\n')

        print('    Deleting...')
        self.cleanDB()

        print('    Inserting...')
        self.insertData()

    def cleanDB(self):
        Member.objects.all().delete()
        Membership_Application.objects.all().delete()
        Membership.objects.all().delete()
        MembershipType.objects.all().delete()
        Identity_Document_Type.objects.all().delete()
        User.objects.all().delete()
        Group.objects.all().delete()
        Permission.objects.all().delete()
        ContentType.objects.all().delete()
        Fine.objects.all().delete()
        FineType.objects.all().delete()
        Promotion.objects.all().delete()
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

        content_type = ContentType.objects.create(app_label='dummy', model='unused')

        permission_usuario = Permission.objects.create(codename='permission_usuario', name='Can Do User Things', content_type=content_type)
        permission_admin = Permission.objects.create(codename='permission_admin', name='Can Do Admin Things', content_type=content_type)
        permission_bungalows = Permission.objects.create(codename='permission_bungalows', name='Can Do Bungalow Things', content_type=content_type)
        permission_eventos = Permission.objects.create(codename='permission_eventos', name='Can Do Event Things', content_type=content_type)
        permission_canchas = Permission.objects.create(codename='permission_canchas', name='Can Do Field Things', content_type=content_type)
        permission_cajero = Permission.objects.create(codename='permission_cajero', name='Can Do Cashier Things', content_type=content_type)
        permission_membresia = Permission.objects.create(codename='permission_membresia', name='Can Do Membership Things', content_type=content_type)
        permission_empresa = Permission.objects.create(codename='permission_empresa', name='Can Do Business Things', content_type=content_type)

        usuario.permissions.add(permission_usuario)  
        bungalows.permissions.add(permission_bungalows)
        eventos.permissions.add(permission_eventos)
        canchas.permissions.add(permission_canchas)
        cajero.permissions.add(permission_cajero)
        membresia.permissions.add(permission_membresia)
        empresa.permissions.add(permission_empresa)

        admin.permissions.add(permission_admin)
        admin.permissions.add(permission_usuario)
        admin.permissions.add(permission_bungalows)
        admin.permissions.add(permission_eventos)
        admin.permissions.add(permission_canchas)
        admin.permissions.add(permission_cajero)
        admin.permissions.add(permission_membresia)
        admin.permissions.add(permission_empresa)

        doc1 = Identity_Document_Type(name='DNI', descripcion='Documento nacional de identidad', status=1)
        doc1.save()

        doc2 = Identity_Document_Type(name='Pasaporte', descripcion='Documento que permite viajar a otros paises',status=1)
        doc2.save()

        mshiptype1 = MembershipType(name='Miembro', guests=5, price=100, billing='Mensual', status=1)
        mshiptype1.save()

        mshiptype2 = MembershipType(name='Empresario', guests=200, price=500, billing='Mensual', status=1)
        mshiptype2.save()

        mshiptype3 = MembershipType(name='Vitalicio', guests=10, price=200, billing='Mensual', status=1)
        mshiptype3.save()

        mship1 = Membership(membership_type=mshiptype1, initialDate=datetime.now(), finalDate=datetime.now() + timedelta(days=30), status=1)
        mship1.save()

        mship2 = Membership(membership_type=mshiptype2, initialDate=datetime.now(), finalDate=datetime.now() + timedelta(days=30), status=1)
        mship2.save()

        mship3 = Membership(membership_type=mshiptype3, initialDate=datetime.now(), finalDate=datetime.now() + timedelta(days=9999), status=1)
        mship3.save()

        mApplication1 = Membership_Application(membership_type=mshiptype1, identity_document_type=doc1, firstName='Enrique',
                                               paternalLastName='Valeriano', maternalLastName='Loli',
                                               document_number=27389283,
                                               comments='Nada que comentar', initialDate=datetime.now() - timedelta(10),
                                               finalDate=datetime.now() - timedelta(5), status=2)

        mApplication1.save()

        mApplication2 = Membership_Application(membership_type=mshiptype2, identity_document_type=doc1, firstName='Jose',
                                               paternalLastName='Luis', maternalLastName='Gil',
                                               document_number=21334473,
                                               comments='Un comentario', initialDate=datetime.now() - timedelta(9),
                                               finalDate=datetime.now() - timedelta(4), status=2)
        mApplication2.save()

        mApplication3 = Membership_Application(membership_type=mshiptype3, identity_document_type=doc1, firstName='Diego',
                                               paternalLastName='Coronado', maternalLastName='Miki',
                                               document_number=22334563,
                                               comments='Overwatch', initialDate=datetime.now() - timedelta(8),
                                               finalDate=datetime.now() - timedelta(3), status=2)
        mApplication3.save()

        mApplication4 = Membership_Application(membership_type=mshiptype1, identity_document_type=doc1, firstName='Jose',
                                               paternalLastName='Pereira', maternalLastName='Nose',
                                               document_number=13382984,
                                               comments='ElPastor', initialDate=datetime.now() - timedelta(2),
                                               finalDate=datetime.now() + timedelta(11), status=1)

        mApplication4.save()

        mApplication5 = Membership_Application(membership_type=mshiptype2, identity_document_type=doc1, firstName='Camila',
                                               paternalLastName='Barboza', maternalLastName='Mendoza',
                                               document_number=83700174,
                                               comments='Campivi', initialDate=datetime.now() - timedelta(1),
                                               finalDate=datetime.now() + timedelta(10), status=1)

        mApplication5.save()

        mApplication6 = Membership_Application(membership_type=mshiptype3, identity_document_type=doc1, firstName='Juan',
                                               paternalLastName='Jose', maternalLastName='Tenorio',
                                               document_number=63890172,
                                               comments='Overwatch', initialDate=datetime.now() - timedelta(8),
                                               finalDate=datetime.now() - timedelta(1), status=0)
        mApplication6.save()

        user1 = User.objects.create_user(username=27389283, email='mailm1@mailcito.com', password='1111')
        usuario.user_set.add(user1)

        memb1 = Member(membership=mship1, identity_document_type=doc1, ubigeo_id=20, user=user1, name='Enrique',
                       paternalLastName='Valeriano', maternalLastName='Loli', document_number=27389283, phone=2394756,
                       email='mailm1@mailcito.com', state=1)
        memb1.save()

        user2 = User.objects.create_user(username=21334473, email='mailm2@mailcito.com', password='1111')
        usuario.user_set.add(user2)

        memb2 = Member(membership=mship2, identity_document_type=doc1, ubigeo_id=40, user=user2, name='Jose',
                       paternalLastName='Luis', maternalLastName='Gil', document_number=21334473, phone=6666666,
                       email='mailm2@mailcito.com', state=1)
        memb2.save()

        user3 = User.objects.create_user(username=22334563, email='mailm3@mailcito.com', password='1111')
        usuario.user_set.add(user3)

        memb3 = Member(membership=mship3, identity_document_type=doc1, ubigeo_id=60, user=user3, name='Diego',
                       paternalLastName='Coronado', maternalLastName='Overwatch', document_number=22334563, phone=1337420,
                       email='mailm3@mailcito.com', state=1)
        memb3.save()

        ftype1 = FineType(reason='Destruccion de silla', price=300, status=1)
        ftype1.save()

        ftype2 = FineType(reason='Destruccion de mesa', price=400, status=1)
        ftype2.save()

        ftype3 = FineType(reason='Falta a reunion comite', price=100, status=1)
        ftype3.save()

        fine1 = Fine(fine_type=ftype1, member=memb2, observations='Destruyo una silla en la cancha A', status='Por Pagar')
        fine1.save()

        fine2 = Fine(fine_type=ftype2, member=memb2,  observations='Destruyo una mesa en la cancha B ',status='Por Pagar')
        fine2.save()

        fine3 = Fine(fine_type=ftype3, member=memb2,  observations='No asistio a una reunion importante',status='Por Pagar')
        fine3.save()

        prom1 = Promotion(description='Promocion venta de bungalows', percentage=15, status=1)
        prom1.save()

        prom2 = Promotion(description='Promocion oferta de membresia', percentage=10, status=1)
        prom2.save()

        prom3 = Promotion(description='Promocion productos todos', percentage=5, status=1)
        prom3.save()

        print('Data has been inserted\n')