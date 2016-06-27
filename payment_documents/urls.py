from django.conf.urls import url
from . import views

app_name = 'checkout'

urlpatterns = [
    url(r'^pay', views.pay, name='pay'),
    url(r'^$', views.index, name='index'),
]
