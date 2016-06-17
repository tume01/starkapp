from django.conf.urls import url
from . import views

app_name = 'bungalowReservations'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post$', views.refresh_table, name='index_post'),
    url(r'^check_in$', views.check_in, name='check_in'),
    url(r'^check_out$', views.check_out, name='check_out'),
    url(r'^accept', views.accept, name='accept'),
    url(r'^cancel', views.cancel, name='cancel'),
    url(r'^create$', views.create_index, name='create_index'),
    url(r'^create/refresh_events$', views.create_refresh_events, name='create_refresh_events'),
    url(r'^create/reserve', views.create_reserve_index, name='create_reserve_index'),
    url(r'^create/post/reserve$', views.create_reserve, name='create_reserve'),
    url(r'^(?P<bungalow_reservation_id>[0-9]+)/update/post$', views.update_bungalow, name='update'),
    url(r'^(?P<bungalow_reservation_id>[0-9]+)/update$', views.update_index, name='update_index'),
    #url(r'^aditional/service/bungalow', views.aditionalServiceBungalowIndex, name='aditional_service'),
]