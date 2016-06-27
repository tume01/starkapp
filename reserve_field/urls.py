from django.conf.urls import url
from . import views

app_name = 'reserve_field'

urlpatterns = [
    url(r'^create/refresh_events$', views.refresh_events, name='create_refresh_events'),
    url(r'^create/reserve/', views.court_show, name='reserve_index'),
    url(r'^create/insert/', views.reservate_court, name='insert'),
    url(r'^create', views.create_index_admin, name='index_admin'),
    url(r'^', views.index, name='index'),
]