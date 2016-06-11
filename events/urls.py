from django.conf.urls import url
from . import views

app_name = 'events'

urlpatterns = [
    url(r'^/create/insert', views.create_event, name='insert'),
    url(r'^/create', views.create_index, name='create_index'),
    url(r'^/edit/insert/(?P<event_id>[0-9]+)', views.update_events, name='update'),
    url(r'^/edit/(?P<event_id>[0-9]+)', views.update_index, name='update_index'),
    url(r'^/register/(?P<event_id>[0-9]+)', views.index_registerUser, name='register_index'),
    url(r'^/register/user/(?P<event_id>[0-9]+)', views.registerUser, name='register'),
    url(r'^/registrations/(?P<event_id>[0-9]+)', views.registrations, name='registrations'),
    url(r'^/registrations/remove/(?P<event_id>[0-9]+)/(?P<member_id>[0-9]+)', views.removeUser, name='remove_user'),
    url(r'^', views.index, name='index'),
]