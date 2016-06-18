from django.conf.urls import url
from . import views

app_name = 'bungalow_type'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]