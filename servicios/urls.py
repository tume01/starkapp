from django.conf.urls import url
from . import views

app_name = 'servicios'

urlpatterns = [
    #url(r'^create/insert', views.create_servicio, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^', views.index, name='index'),
]