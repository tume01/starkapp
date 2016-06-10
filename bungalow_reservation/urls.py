from django.conf.urls import url
from . import views

app_name = 'bungalowReservation'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.refresh_table, name='index_post'),
    url(r'^check_in$', views.check_in, name='check_in'),
    url(r'^check_out$', views.check_out, name='check_out'),
    url(r'^create/post', views.create_bungalow_reservation, name='create'),
    url(r'^create', views.create_index_admin, name='create_index'),
    url(r'^(?P<bungalow_reservation_id>[0-9]+)/update/post', views.update_bungalow, name='update'),
    url(r'^(?P<bungalow_reservation_id>[0-9]+)/update', views.update_index, name='update_index'),
]