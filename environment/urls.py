from django.conf.urls import url
from . import views

app_name = 'environment'

urlpatterns = [
    url(r'^book/index', views.index_book, name='index_book'),
    url(r'^book/create', views.create_reservation, name='create_reservation'),
    url(r'^book/create/post', views.create_reservation_post, name='create_reservation_post'),
    url(r'^book/create/getEnvs', views.create_reservation_getEnvs, name='create_reservation_getEnvs'),
    url(r'^book/create/insert', views.insert_reservation, name='insert_reservation'),
    """
    url(r'^(?P<bungalow_reservation_id>[0-9]+)/update/post', views.update_bungalow, name='update'),
    url(r'^(?P<bungalow_reservation_id>[0-9]+)/update', views.update_index, name='update_index'),
    """
    url(r'^create/insert', views.create_environment, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/insert', views.edit_environment, name='edit'),
    url(r'^edit', views.edit_index, name='edit_index'),
    url(r'^delete', views.delete_environment, name='delete'),
    url(r'^', views.index, name='index'),
]