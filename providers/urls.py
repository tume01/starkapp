from django.conf.urls import url
from . import views

app_name = 'providers'

urlpatterns = [
    url(r'^create/insert', views.create_provider, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/(?P<id>\d+)$', views.edit_index, name='edit'),
    url(r'^edit/update', views.edit_provider, name='update'),
    url(r'^', views.index, name='index'),
]