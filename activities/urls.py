from django.conf.urls import url
from . import views

app_name = 'activities'

urlpatterns = [
    url(r'^/create/insert', views.create_activity, name='insert'),
    url(r'^/create', views.create_index, name='create_index'),
    url(r'^', views.index, name='index'),
]