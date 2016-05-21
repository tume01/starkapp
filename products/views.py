from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.ProductsService import ProductsService
from services.ProductTypesService import ProductTypesService
from services.ProvidersService import ProvidersService
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET'])
def index(request):

    product_service = ProductsService()

    products = product_service.getProducts()

    context = {
        'products' : products,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Products/index_product.html', context) 

@require_http_methods(['GET'])
def create_index(request):

    providers_service = ProvidersService()
    providers = providers_service.getActiveProviders()

    product_types_service = ProductTypesService()
    product_types = product_types_service.getProductTypes()

    context = {
        'product_types' : product_types,
        'providers' : providers,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Products/new_product.html', context)

@require_http_methods(['POST'])
def create_product(request):

    insert_data = {}

    insert_data["name"] = request.POST['name']

    insert_data["description"] = request.POST['description']

    insert_data["price"] = request.POST['price']

    insert_data["anual_price"] = request.POST['anual_price']

    insert_data["minimum_price"] = request.POST['minimum_price']

    insert_data["status"] = request.POST['status']

    insert_data["product_type_id"] = request.POST['product_type_id']

    product_service = ProductsService()

    product_service.create(insert_data)

    return HttpResponseRedirect(reverse('products:index'))
