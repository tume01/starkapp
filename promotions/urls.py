from django.conf.urls import url
from . import views

app_name = 'promotions'

urlpatterns = [
    url(r'^create/insert', views.create_promotion, name='insert'),
    url(r'^create', views.create_promotion, name='create_index'),
    url(r'^edit/insert', views.create_promotion, name='edit'),
    url(r'^edit', views.create_promotion, name='edit_index'),
    url(r'^delete', views.create_promotion, name='delete'),
    url(r'^', views.index, name='index'),
]