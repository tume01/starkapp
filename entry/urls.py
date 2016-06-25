from django.conf.urls import url
from . import views

app_name = 'entry'

urlpatterns = [

    url(r'^create/insert', views.insert, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^verify', views.verify_member, name='verify_member'),
    url(r'^filter', views.index_filter, name='filter'),
    url(r'^', views.index, name='index'),

]
