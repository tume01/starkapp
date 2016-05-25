from django.conf.urls import url
from . import views

app_name = 'activities'

urlpatterns = [
    url(r'^create/insert', views.create_activity, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^update/(?P<activity_id>[0-9]+)', views.update_index, name='select'),
    url(r'^save/(?P<activity_id>[0-9]+)', views.update, name='update'),
    url(r'^', views.index, name='index'),
]