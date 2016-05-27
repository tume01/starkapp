from django.conf.urls import url
from . import views

app_name = 'guests'

urlpatterns = [
    url(r'^create/insert', views.create_guest, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/insert', views.edit_guest, name='edit'),
    url(r'^edit', views.edit_index, name='edit_index'),
]