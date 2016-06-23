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
    url(r'^admin/create/insert', views.admin_create_affiliate, name='admin_insert'),
    url(r'^admin/create', views.admin_create_index, name='admin_create_index'),
    url(r'^admin/edit/insert', views.admin_edit_affiliate, name='admin_edit'),
    url(r'^admin/edit', views.admin_edit_affiliate_index, name='admin_edit_index'),
    url(r'^admin/delete', views.admin_delete_affiliate, name='admin_delete'),
    url(r'^admin/move', views.admin_move_affiliate, name='admin_move'),
    url(r'^admin', views.admin_affiliate_index, name='admin_index'),
    url(r'^', views.affiliate_index, name='index'),

]
    
