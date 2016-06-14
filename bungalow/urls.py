from django.conf.urls import url
from . import views

app_name = 'bungalow'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.refresh_table, name='index_post'),
    url(r'^create/post', views.create_bungalow, name='create'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^(?P<bungalow_id>[0-9]+)/update/post', views.update_bungalow, name='update'),
    url(r'^(?P<bungalow_id>[0-9]+)/update', views.update_index, name='update_index'),
]