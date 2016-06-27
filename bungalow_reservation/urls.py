from django.conf.urls import url
from . import views

app_name = 'bungalowReservation'

urlpatterns = [
    # Ajax
    url(r'^check_in$', views.check_in, name='check_in'),
    url(r'^check_out$', views.check_out, name='check_out'),
    url(r'^accept$', views.accept, name='accept'),
    url(r'^cancel$', views.cancel, name='cancel'),

    # Admin
    url(r'^$', views.admin_index, name='admin_index'),
    url(r'^admin_post$', views.admin_refresh_table, name='index_post'),
    url(r'^admin_create$', views.admin_create_index, name='admin_create_index'),
    url(r'^admin_create/refresh_events$', views.admin_create_refresh_events, name='admin_create_refresh_events'),
    url(r'^admin_create/reserve', views.admin_create_reserve_index, name='admin_create_reserve_index'),
    url(r'^admin_create/post/reserve$', views.admin_create_reserve, name='admin_create_reserve'),

    # User
    url(r'^index$', views.user_index, name='user_index'),
    url(r'^post$', views.user_refresh_table, name='index_post'),
    url(r'^create$', views.user_create_index, name='user_create_index'),
    url(r'^create/refresh_events$', views.user_create_refresh_events, name='user_create_refresh_events'),
    url(r'^create/reserve', views.user_create_reserve_index, name='user_create_reserve_index'),
    url(r'^create/post/reserve$', views.user_create_reserve, name='user_create_reserve'),

    # IDK
    url(r'^aditional/service/bungalow', views.aditionalServiceBungalowIndex, name='aditional_service'),
    url(r'^filter/aditional/services/(?P<id>\d+)$', views.filterAditionalServiceBungalow, name='filter_service'),
    url(r'^save/aditional/services/(?P<bungalow_id>\d+)$', views.saveAditionalServiceBungalow, name='save_service'),

    # Unimplemented
    url(r'^(?P<bungalow_reservation_id>[0-9]+)/update/post$', views.update_bungalow, name='update'),
    url(r'^(?P<bungalow_reservation_id>[0-9]+)/update$', views.update_index, name='update_index'),
]