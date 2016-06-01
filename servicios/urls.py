from django.conf.urls import url
from . import views

app_name = 'servicios'

urlpatterns = [
    url(r'^create/insert', views.create_servicio, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^update/insert/(?P<servicio_id>[0-9]+)', views.update_servicio, name='update'),
    url(r'^update/(?P<servicio_id>[0-9]+)', views.update_index, name='update_index'),
    url(r'^delete/(?P<servicio_id>[0-9]+)', views.delete, name='delete'),
    url(r'^', views.index, name='index'),
]