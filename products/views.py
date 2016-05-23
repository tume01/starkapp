from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.ProductsService import ProductsService
from services.ProductTypesService import ProductTypesService
from services.ProvidersService import ProvidersService
from django.views.decorators.http import require_http_methods

import json

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
    req = json.loads( request.body.decode('utf-8') )

    insert_data["name"] = req.get("name")
    insert_data["minimum_stock"] = req.get("minStock")
    insert_data["actual_stock"] = req.get("actualStock")
    insert_data["description"] = req.get("description")
    #insert_data["provider"] = req.get("providers")
    insert_data["price"] = req.get("price")
    insert_data["status"] = 1 #1 means active

    product_types_service = ProductTypesService()
    product_type = product_types_service.find(req.get("productType"))
    insert_data["product_type"] = product_type

    product_service = ProductsService()
    product_service.create(insert_data)  

    providers_service = ProvidersService() 
    list_providers = []

    for i in req.get("providers"):
        list_providers.add(providers_service.find(i))
   

    print(list_providers)

    return HttpResponse(req)
    #return HttpResponseRedirect(reverse('products:index'))
