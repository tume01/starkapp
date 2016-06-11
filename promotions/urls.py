from django.conf.urls import url
from . import views

app_name = 'promotions'

urlpatterns = [
    url(r'^create/insert', views.create_promotion, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/insert', views.edit_promotion, name='edit'),
    url(r'^edit', views.edit_index, name='edit_index'),
    url(r'^delete', views.delete_promotion, name='delete'),
    url(r'^filter', views.filter, name='filter'),
    url(r'^', views.index, name='index'),
]