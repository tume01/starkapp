from django.conf.urls import url
from . import views

app_name = 'ubigeo'

urlpatterns = [
    url(r'^distritos', views.get_distritos, name='distritos'),
    url(r'^provincias', views.get_provincias, name='provincias'),
]