from django.conf.urls import url
from . import views

app_name = 'providers'

urlpatterns = [
	url(r'^create/insert/concesionary', views.create_concesionary, name='insert_concesionary'),
	url(r'^create/concesionary', views.create_index_concesionary, name='create_index_concesionary'),
	url(r'^edit/concesionary/(?P<id>\d+)$', views.edit_index_concesionary, name='edit_concesionary'),
    url(r'^create/insert', views.create_provider, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/(?P<id>\d+)$', views.edit_index, name='edit'),
    url(r'^edit/(?P<id>\d+)/update', views.edit_provider, name='update'),
    url(r'^filter', views.filter_product, name='filter'),
    url(r'^concesionary', views.index_concesionary, name='index_concesionary'),
    url(r'^', views.index, name='index'),
]