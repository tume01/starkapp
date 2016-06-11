from django.conf.urls import url
from . import views

app_name = 'affiliate'

urlpatterns = [
    url(r'^create/insert', views.create_affiliate, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/insert', views.edit_affiliate, name='edit'),
    url(r'^edit', views.edit_affiliate_index, name='edit_index'),
    url(r'^delete', views.delete_affiliate, name='delete'),
    url(r'^verify', views.verify_affiliate, name='verify_affiliate'),
    url(r'^', views.affiliate_index, name='index'),

]
