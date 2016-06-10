from django.conf.urls import url
from . import views

app_name = 'reserve_field'

urlpatterns = [
    url(r'^create/refresh_field', views.refresh_field, name='create_refresh_field'),
    url(r'^create/refresh_hour', views.refresh_hour, name='create_refresh_hour'),
    url(r'^create/refresh_max_time', views.refresh_max_time, name='create_refresh_max_time'),
    url(r'^create/insert', views.reservate_court, name='insert'),
    url(r'^', views.index, name='index'),
]