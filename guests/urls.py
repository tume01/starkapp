from django.conf.urls import url
from . import views

app_name = 'guests'

urlpatterns = [
    url(r'^create/insert', views.create_guest, name='insert'),
    url(r'^create', views.create_guest, name='create_index'),
    url(r'^edit/insert', views.edit_guest, name='edit'),
    url(r'^edit', views.edit_guest, name='edit_index'),
    url(r'^delete', views.delete_guest, name='delete'),
    url(r'^', views.index, name='index'),
]