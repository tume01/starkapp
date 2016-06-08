from django.conf.urls import url
from . import views

app_name = 'suspension'

urlpatterns = [
    url(r'^create/insert', views.create_suspension, name='insert'),
    url(r'^create', views.create_suspension_index, name='create_index'),
    url(r'^edit/insert', views.edit_suspension, name='edit'),
    url(r'^edit', views.edit_suspension_index, name='edit_index'),
    url(r'^delete', views.delete_suspension, name='delete'),
    url(r'^', views.suspension_index, name='index'),
    url(r'^filter', views.suspension_filter, name='filter'),
]