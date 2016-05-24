from django.conf.urls import url
from . import views

app_name = 'bungalows'

urlpatterns = [
    url(r'^create/insert', views.create_bungalow, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^update/insert/(?P<bungalow_id>[0-9]+)', views.update_bungalow, name='update'),
    url(r'^update/(?P<bungalow_id>[0-9]+)', views.update_index, name='update_index'),
    url(r'^', views.index, name='index'),
]