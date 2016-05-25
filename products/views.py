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
    insert_data["price"] = req.get("price")
    insert_data["status"] = 1 #1 means active

    product_types_service = ProductTypesService()
    product_type = product_types_service.find(req.get("productType"))
    insert_data["product_type"] = product_type

    product_service = ProductsService()
    pr = product_service.create(insert_data)  

    providers_service = ProvidersService() 
    list_providers = []

    for i in req.get("providers"):
        list_providers.append(providers_service.find(i))

    insert_data["provider"] = list_providers
    product_service.update(pr.id, insert_data)
   
    return HttpResponse(json.dumps(req), content_type='application/json')

@require_http_methods(['GET'])
def edit_index(request, id):

    product_service = ProductsService()
    product_type_service = ProductTypesService()
    provider_service = ProvidersService()


    product = product_service.find(id)
    all_providers = provider_service.getActiveProviders()
    all_product_types = product_type_service.getProductTypes()

    context = {
        'product' : product,
        'all_providers' : all_providers,
        'all_product_types' : all_product_types,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Products/edit_product.html', context)

@require_http_methods(['POST'])
def edit_product(request, id):

    update_data = {}
    req = json.loads( request.body.decode('utf-8') )

    update_data["name"] = req.get("name")
    update_data["minimum_stock"] = req.get("minStock")
    update_data["actual_stock"] = req.get("actualStock")
    update_data["description"] = req.get("description")
    update_data["price"] = req.get("price")

    product_types_service = ProductTypesService()
    product_type = product_types_service.find(req.get("productType"))
    update_data["product_type"] = product_type

    product_service = ProductsService()
    pr = product_service.update(id, update_data) 

    return HttpResponse(json.dumps(req), content_type='application/json')