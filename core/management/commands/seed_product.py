from django.core.management.base import BaseCommand
#from product_types.models import *
from products.models import *
from providers.models import *
from datetime import datetime,timedelta

class Command(BaseCommand):
    help = 'This command will seed the database (Product, Provider and Product Types)'

    def handle(self, *args, **options):
        print('\n  Product Seeder is running...\n')

        print('    Deleting...')
        cleanProduct()

        print('    Inserting...')
        insertProduct()

def cleanProduct():
    ProductType.objects.all().delete()
    Product.objects.all().delete()
    ProviderType.objects.all().delete()
    Provider.objects.all().delete()
    print('    Data has been deleted\n')

def insertProduct():

    prt1 = ProviderType(name= 'Proveedor', description= 'Proveedor de productos en general.')
    prt1.save()

    prt2 = ProviderType(name= 'Concesionario', description= 'Proveedor de servicios  alimenticios.')
    prt2.save()


    pt1 = ProductType(name= 'Merchandising', description= 'Productos para libre venta a miembros.')
    pt1.save()

    pt2 = ProductType(name= 'Accesorios', description= 'Productos destinados al inventario del club.')
    pt2.save()

    pt3 = ProductType(name= 'Extra', description= 'Productos extra')
    pt3.save()

    pr1 = Provider(status=1, ruc=10103632728, businessName='P&G S.A.', region='Lima', 
                   province='Lima', distric='Lima', registrationDate=datetime.now(), 
                   address='Av. Abancay 522', phone=8264837, postal=62737, email='bramirez@pyg.com', 
                   contactName='Bruno Ramirez', contactPhone=972633258, provider_type=prt1, vigencyDate=datetime.now()+timedelta(days=30))
    pr1.save()

    pr2 = Provider(status=1, ruc=10922632728, businessName='Unilever S.A.', region='Lima', 
                   province='Lima', distric='Lima', registrationDate=datetime.now(), 
                   address='Av. Abancay 522', phone=8264837, postal=62737, email='jpineda@unilever.com', 
                   contactName='Jenny Pineda', contactPhone=972633258, provider_type=prt1, vigencyDate=datetime.now()+timedelta(days=30))
    pr2.save()

    pr3 = Provider(status=1, ruc=10103600028, businessName='Nestle S.A.', region='Lima', 
                   province='Lima', distric='Lima', registrationDate=datetime.now(), 
                   address='Av. Abancay 522', phone=8264837, postal=62737, email='aperez@nestle.com', 
                   contactName='Alfredo Perez', contactPhone=972633258, provider_type=prt1, vigencyDate=datetime.now()+timedelta(days=30))
    pr3.save()

    pr4 = Provider(status=1, ruc=10003600028, businessName='Food Court S.A.', region='Lima', 
                   province='Lima', distric='Lima', registrationDate=datetime.now(), 
                   address='Av. Abancay 522', phone=8264837, postal=62737, email='aperez@fcourt.com', 
                   contactName='Alfredo Perez', contactPhone=972633258, provider_type=prt2, vigencyDate=datetime.now()+timedelta(days=30))
    pr4.save()

    pr5 = Provider(status=1, ruc=10872400028, businessName='Sodexo S.A.', region='Lima', 
                   province='Lima', distric='Lima', registrationDate=datetime.now(), 
                   address='Av. Abancay 522', phone=8264837, postal=62737, email='aperez@sodexo.com', 
                   contactName='Alfredo Perez', contactPhone=972633258, provider_type=prt2, vigencyDate=datetime.now()+timedelta(days=30))
    pr5.save()

    list_providers_1 = []
    list_providers_2 = []
    list_providers_3 = []

    list_providers_1.append(pr1)
    list_providers_1.append(pr2)

    list_providers_2.append(pr2)
    list_providers_2.append(pr3)

    list_providers_3.append(pr1)
    list_providers_3.append(pr2)
    list_providers_3.append(pr3)


    a1 = Product(product_type=pt1, price=40, actual_stock=100, minimum_stock=10, status=0, description='Llaveros de plastico', name='Llaveros', deleted_at=None)
    a1.save()
    a1.provider = list_providers_1
    a1.save()

    a2 = Product(product_type=pt2, price=50, actual_stock=100, minimum_stock=10, status=0, description='Bufandas a base de lana de alpaca', name='Bufandas', deleted_at=None)
    a2.save()
    a2.provider = list_providers_2
    a2.save()

    a3 = Product(product_type=pt3, price=20, actual_stock=100, minimum_stock=10, status=0, description='Lentes de sol con proteccion UV 100', name='Lentes de sol', deleted_at=None)
    a3.save()
    a3.provider = list_providers_3
    a3.save()

    print('    Data has been inserted\n')

