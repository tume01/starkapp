from django.conf.urls import url
from . import views

app_name = 'fine'

urlpatterns = [
    url(r'^type/create/insert', views.create_type, name='insert_type'),
    url(r'^type/create', views.create_type_index, name='create_type_index'),
    url(r'^type/edit/insert', views.edit_type, name='edit_type'),
    url(r'^type/edit', views.edit_type_index, name='edit_type_index'),
    url(r'^type/delete', views.delete_type, name='delete_type'),
    url(r'^type', views.type_index, name='index_type'),
]