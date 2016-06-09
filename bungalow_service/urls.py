from django.conf.urls import url
from . import views

app_name = 'bungalow_service'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getServices/(?P<id>\d+)$', views.getServices, name='getServices'),
]
