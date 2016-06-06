from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [
    url(r'^type/create/insert', views.create_user_type, name='type/insert'),
    url(r'^type/create', views.create_user_type_index, name='type/create_index'),
    url(r'^type/edit/insert', views.edit_user_type, name='type/edit'),
    url(r'^type/edit', views.edit_user_type_index, name='type/edit_index'),
    url(r'^type', views.user_type_index, name='type/index'),
    url(r'^edit/insert', views.edit_user, name='edit'),
    url(r'^member', views.edit_user_member, name='edit_user_member'),
    url(r'^edit', views.edit_user_index, name='edit_index'),
    url(r'^verify/member', views.verify_user_member, name='verify_user_member'),
    url(r'^verify', views.verify_user, name='verify_user'),
    url(r'^create/insert', views.create_user, name='insert'),
    url(r'^create', views.create_user_index, name='create_index'),
    url(r'^', views.user_index, name='index'),

]