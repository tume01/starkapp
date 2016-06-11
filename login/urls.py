from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url(r'^login/$', views.login_view, name= 'login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^iniUser', views.iniUser, name='iniUser'),
    url(r'^iniAdmin', views.iniAdmin, name='iniAdmin'),
    url(r'^', views.index, name='index'),


]
