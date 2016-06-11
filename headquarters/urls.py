from django.conf.urls import url

from . import views

app_name = 'headquarters'

urlpatterns = [    
    url(r'^create/insert', views.create_headquarters, name='create_insert'),
    url(r'^create', views.create_headquarters_index, name='create_index'),
    
	url(r'^update/(?P<headquarter_id>[0-9]+)', views.update_headquarters_index, name='select'),
    url(r'^save/(?P<headquarter_id>[0-9]+)', views.update_headquarters, name='update'),

    url(r'^delete/(?P<headquarter_id>[0-9]+)', views.delete, name='delete'),

    url(r'^', views.index, name='index'),
]