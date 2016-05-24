from django.conf.urls import url
from . import views

app_name = 'eventstype'

urlpatterns = [
    url(r'^/create/insert', views.create_eventstype, name='insert'),
    url(r'^/create', views.create_index, name='create_index'),
    url(r'^/edit/(?P<type_id>[0-9]+)/$', views.update, name='create_index'),
    url(r'^', views.index, name='index'),
]