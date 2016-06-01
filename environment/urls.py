from django.conf.urls import url
from . import views

app_name = 'environment'

urlpatterns = [
    url(r'^create/insert', views.create_environment, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^update/(?P<id>[0-9]+)', views.edit_environment, name='edit'),
    url(r'^edit/(?P<id>[0-9]+)', views.edit_index, name='edit_index'),
    url(r'^delete', views.delete_environment, name='delete'),
    url(r'^', views.index, name='index'),
]