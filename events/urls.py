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
    url(r'^/signupUser/(?P<event_id>[0-9]+)', views.userSignup, name='signup'),
    url(r'^/signoutUser/(?P<event_id>[0-9]+)', views.userSignout, name='signout'),
    url(r'^/signup/(?P<event_id>[0-9]+)', views.select_userEvent, name='userEvent_select'),
    url(r'^/myEvents', views.index_UserEvents, name='userEvents_index'),
    url(r'^/signup', views.index_UserSignup, name='userSignup_index'),
    url(r'^', views.index, name='index'),
]