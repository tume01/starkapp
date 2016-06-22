from django.conf.urls import url
from . import views

app_name = 'activities'

urlpatterns = [
    url(r'^create/insert', views.create_activity, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^update/(?P<activity_id>[0-9]+)', views.update_index, name='select'),
    url(r'^members/(?P<activity_id>[0-9]+)', views.index_members, name='members'),
    url(r'^members/add/(?P<activity_id>[0-9]+)/insert', views.add_member, name='insert_member'),
    url(r'^members/add/(?P<activity_id>[0-9]+)', views.index_add_member, name='add_member'),
    url(r'^members/remove/(?P<activity_id>[0-9]+)/(?P<member_id>[0-9]+)', views.remove_member, name='member_remove'),
    url(r'^save/(?P<activity_id>[0-9]+)', views.update, name='update'),
    url(r'^delete/(?P<activity_id>[0-9]+)', views.delete, name='delete'),
    url(r'^signupUser/(?P<activity_id>[0-9]+)', views.signup, name='signup'),
    url(r'^signup/(?P<activity_id>[0-9]+)', views.select_signUp, name='select_signup'),
    url(r'^signout/(?P<activity_id>[0-9]+)', views.signout, name='signout'),
    url(r'^userActivities', views.user_activities, name='user_activities'),
    url(r'^signup', views.index_signUp, name='index_signup'),
    url(r'^', views.index, name='index'),
]