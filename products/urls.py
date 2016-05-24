from django.conf.urls import url
from . import views

app_name = 'products'

urlpatterns = [
    url(r'^create/insert', views.create_product, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/(?P<pk>\d+)$', views.update_product, name='edit'),
    url(r'^', views.index, name='index'),
]