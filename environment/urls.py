from django.conf.urls import url
from . import views

app_name = 'environment'

urlpatterns = [
    url(r'^book/index', views.index_book, name='index_book'),
    """
    url(r'^post$', views.index_filters, name='index_post'),
    url(r'^check_in$', views.check_in, name='check_in'),
    url(r'^check_out$', views.check_out, name='check_out'),
    url(r'^create/post', views.create_bungalow, name='create'),
    url(r'^create', views.create_index, name='create_index'),
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