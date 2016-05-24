from django.conf.urls import url
from . import views

app_name = 'membership_application'

urlpatterns = [
    url(r'^create/insert', views.create_membership_application, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/insert', views.edit_membership_application, name='edit'),
    url(r'^edit', views.edit_index, name='edit_index'),
    url(r'^delete', views.delete_membership_application, name='delete'),
    url(r'^approve', views.approve_membership_application, name='approve'),
    url(r'^filter', views.filter, name='filter'),
    url(r'^user/filter', views.user_filter, name='user_filter'),
    url(r'^user', views.user_index, name='user_index'),

    url(r'^objection/index', views.objection_index, name='objection_index'),
    url(r'^objection/insert', views.create_objection, name='objection_insert'),

    url(r'^index', views.index, name='index'),

]