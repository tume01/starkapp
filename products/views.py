from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from services.ProductsService import ProductsService
from services.ProductTypesService import ProductTypesService
from services.ProvidersService import ProvidersService
from django.views.decorators.http import require_http_methods

from products.models import Product

import json
import urllib
import logging
from django.db import IntegrityError, transaction

@require_http_methods(['GET'])
def index(request):

    product_service = ProductsService()
    providers_service = ProvidersService()
    product_types_service = ProductTypesService()

    products = product_service.getProducts()
    all_providers = providers_service.getActiveProviders()
    all_product_types = product_types_service.getProductTypes()

    context = {
        'products' : products,
        'all_providers' : all_providers,
        'all_product_types' : all_product_types,
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

    providers_service = ProvidersService() 
    list_providers = []

    for i in req.get("providers"):
        list_providers.append(providers_service.find(i))

    update_data["provider"] = list_providers

    product_service = ProductsService()
    pr = product_service.update(id, update_data) 

    return HttpResponse(json.dumps(req), content_type='application/json')

@require_http_methods(['GET'])
def delete_product(request, id):

    product_service = ProductsService()
    product = product_service.find(id)
    
    update_data = {}

    update_data["name"] = product.name
    update_data["minimum_stock"] = product.minimum_stock
    update_data["actual_stock"] = product.actual_stock
    update_data["description"] = product.description
    update_data["price"] = product.price

    product_types_service = ProductTypesService()
    product_type = product_types_service.find(product.product_type.id)
    #print(product.product_type.id)

    update_data["product_type"] = product_type

    providers_service = ProvidersService() 
    list_providers = []

    #print(product.provider.all)
    for i in product.provider.all():
        list_providers.append(providers_service.find(i.id))

    update_data["provider"] = list_providers

    update_data["status"] = 0 #0 means inactive

    product_service = ProductsService()
    product_service.update(id, update_data) 
    
    

    return HttpResponseRedirect(reverse('products:index'))

@require_http_methods(['POST'])
def filter_product(request):
    filter_data = {}
    req = json.loads( request.body.decode('utf-8') )

    print(req.get("f_selectProductType"))

    
    qry = 'SELECT * FROM products_product WHERE id<2'


    logging.debug(qry)

    try:
        for p in Product.objects.raw(qry):
            print(p.id)

        #list_products = list_products[:]
    except IntegrityError:
        handle_exception()
        list_products = None


    

    return HttpResponse( json.dumps(req), content_type='application/json')