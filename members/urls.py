from django.conf.urls import url
from . import views

app_name = 'members'

urlpatterns = [
    url(r'^edit/insert', views.edit_member, name='edit'),
    url(r'^edit', views.edit_member_index, name='edit_index'),
    url(r'^delete', views.delete_member, name='delete'),
    url(r'^', views.member_index, name='index'),

]