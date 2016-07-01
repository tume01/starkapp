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
from django.core import serializers

@require_http_methods(['GET'])
def index(request):

    product_service = ProductsService()
    providers_service = ProvidersService()
    product_types_service = ProductTypesService()

    filters = {}
    filters['status'] = "1"
    products = product_service.filter(filters)
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

@require_http_methods(['POST'])
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

    print("nombre= "+req.get("f_name"))
    print(req.get("f_select2Provider"))
    print("tipo= "+req.get("f_selectProductType"))

    product_name = ""

    qry = "SELECT p.id, p.price, p.actual_stock, p.minimum_stock, p.status, p.description, p.name, p.product_type_id "
    qry += " FROM products_product p, products_product_provider pxp WHERE p.id = pxp.product_id "


    if req.get("f_selectProductType") == '0' and req.get("f_name") == '' and req.get("f_select2Provider") == None:
        print("sin filtro")
    else:
        if req.get("f_selectProductType") != '0':
            qry += " AND p.product_type_id="+req.get("f_selectProductType") + " "
        
        if req.get("f_select2Provider") != None:
            i=0
            for prov_id in req.get("f_select2Provider"):
                if i == 0:
                    qry += " AND ( pxp.provider_id="+ prov_id + " "
                    i += 1
                else:
                    qry += " OR pxp.provider_id="+ prov_id + " "

            qry += " ) "

        if req.get("f_name") != '':
            qry += " AND p.name LIKE %s"
            product_name = req.get("f_name")

    print("qry= "+qry)

    req_list = []

    try:
        if product_name != '':
            list_products = Product.objects.raw(qry, [product_name])
        else:
            list_products = Product.objects.raw(qry)
        
        for p in list_products:
            data_item = {}
            data_item["id"] = p.id
            data_item["name"] = p.name
            data_item["price"] = p.price
            data_item["actual_stock"] = p.actual_stock
            data_item["minimum_stock"] = p.minimum_stock
            data_item["status"] = p.status
            data_item["description"] = p.description
            #data_item["id"] = p.id
            req_list.append(data_item)

    except IntegrityError:
        handle_exception()
        list_products = None

    return HttpResponse( json.dumps(req_list), content_type='application/json')

@require_http_methods(['GET'])
def index_in_out(request):

    product_service = ProductsService()
    providers_service = ProvidersService()
    product_types_service = ProductTypesService()

    products = product_service.getProducts()
    all_providers = providers_service.getActiveProviders()
    all_product_types = product_types_service.getProductTypes()

    context = {
        'products' : products,
        #'all_providers' : all_providers,
        'all_product_types' : all_product_types,
        'titulo' : 'titulo'
    }

    return render(request, 'Admin/Products/index_in_out.html', context) 

@require_http_methods(['POST'])
def register_in_out(request, id):
    update_data = {}
    req = json.loads( request.body.decode('utf-8') )
    req_send = ""

    product_service = ProductsService()

    q = int(req.get("quantity"))

    p = product_service.find(id)

    

    if (p.actual_stock >= q and req.get("move") == '1') or req.get("move") == '0':
        update_data["name"] = p.name
        update_data["minimum_stock"] = p.minimum_stock

        if req.get("move") == '1': #salida
            update_data["actual_stock"] = p.actual_stock - q
        else:
            update_data["actual_stock"] = p.actual_stock + q

        update_data["description"] = p.description
        update_data["price"] = p.price

        product_types_service = ProductTypesService()
        product_type = product_types_service.find(p.product_type.id)
        update_data["product_type"] = product_type

        providers_service = ProvidersService() 
        list_providers = []

        for i in p.provider.all():
            list_providers.append(providers_service.find(i.id))

        update_data["provider"] = list_providers

        
        pr = product_service.update(id, update_data)

        req_send = "0"
    else:
        req_send += str(p.actual_stock)

    return HttpResponse( json.dumps(req_send), content_type='application/json')


@require_http_methods(['GET'])
def index_shop_products(request):
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

    return render(request, 'User/Products/index_shop_products.html', context) 


@require_http_methods(['POST'])
def make_purchase(request):
    req = json.loads( request.body.decode('utf-8') )
    update_data = {}

    product = ProductsService().find(req.get("id"))

    update_data["product_type"] = product.product_type
    update_data["provider"] = product.provider.all()
    #purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    update_data["price"] = product.price
    update_data["actual_stock"] = product.actual_stock - int(req.get("quantity"))
    update_data["minimum_stock"] = product.minimum_stock
    update_data["status"] = product.status
    update_data["description"] = product.description
    update_data["name"] = product.name

    ProductsService().update(req.get("id"), update_data)

    return HttpResponse( json.dumps(req), content_type='application/json')
