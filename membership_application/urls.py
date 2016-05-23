from django.conf.urls import url
from . import views

app_name = 'membership_application'

urlpatterns = [
    url(r'^create/insert', views.create_membership_application, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^edit/insert', views.edit_membership_application, name='edit'),
    url(r'^edit', views.edit_index, name='edit_index'),
    url(r'^delete', views.delete_membership_application, name='delete'),
    url(r'^filter', views.filter, name='filter'),
    url(r'^', views.index, name='index'),
    url(r'^user', views.index_user, name='index_user'),
    url(r'^user/filter', views.filter_user, name='user_filter'),

    url(r'^objection/insert', views.create_objection, name='objection_insert'),
    url(r'^objection', views.objection_index, name='objection_index'),
]