from django.conf.urls import url
from . import views

app_name = 'promotions'

urlpatterns = [
	url(r'^getmembership',views.get_membership,name="get_membership"),
	url(r'^getbungalows',views.get_bungalows,name="get_bungalows"),
	url(r'^getevents',views.get_events,name="get_events"),
    url(r'^create/insert', views.create_promotion, name='insert'),
    url(r'^create', views.create_index, name='create_index'),
    url(r'^editMembership/insert', views.edit_promotion_membership, name='edit_membership'),
    url(r'^editBungalow/insert', views.edit_promotion_bungalow, name='edit_bungalow'),
    url(r'^editEvent/insert', views.edit_promotion_event, name='edit_event'),
    url(r'^listMembership', views.list_promotion_membership, name='list_membership'),
    url(r'^listBungalow', views.list_promotion_bungalow, name='list_bungalow'),
    url(r'^listEvent', views.list_promotion_event, name='list_event'),
    url(r'^editMembership', views.index_edit_promotion_membership, name='index_edit_membership'),
    url(r'^editBungalow', views.index_edit_promotion_bungalow, name='index_edit_bungalow'),
    url(r'^editEvent', views.index_edit_promotion_event, name='index_edit_event'),
    url(r'^delete', views.delete_promotion, name='delete'),
    url(r'^filter', views.filter, name='filter'),
    url(r'^', views.index, name='index'),
]