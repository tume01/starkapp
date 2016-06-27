from django.conf.urls import url
from . import views

app_name = 'politics'

urlpatterns = [
    url(r'^create/insert', views.create_politic, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^update/insert/(?P<politic_id>[0-9]+)', views.update_politic, name='update'),
    url(r'^update/(?P<politic_id>[0-9]+)', views.update_index, name='update_index'),
    url(r'^delete/(?P<politic_id>[0-9]+)', views.delete, name='delete'),
    url(r'^', views.index, name='index'),
]