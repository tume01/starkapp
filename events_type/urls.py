from django.conf.urls import url
from . import views

app_name = 'events_type'

urlpatterns = [
    url(r'^create/insert', views.create_eventstype, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/insert/(?P<type_id>[0-9]+)', views.update_eventstype, name='update'),
    url(r'^edit/(?P<type_id>[0-9]+)', views.update_index, name='update_index'),
    url(r'^', views.index, name='index'),
]


