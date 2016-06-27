from django.conf.urls import url
from . import views

app_name = 'products'

urlpatterns = [
	url(r'^make/purchase', views.make_purchase, name='make_purchase'),
	url(r'^index/shop/product', views.index_shop_products, name='index_shop_products'),
	url(r'^register_in_out/(?P<id>\d+)$', views.register_in_out, name='register_in_out'),
	url(r'^index_in_out', views.index_in_out, name='index_in_out'),
    url(r'^create/insert', views.create_product, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/(?P<id>\d+)$', views.edit_index, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.edit_product, name='update'),
    url(r'^delete/update/(?P<id>\d+)$', views.delete_product, name='delete'),
    url(r'^filter', views.filter_product, name='filter'),
    url(r'^', views.index, name='index'),
]