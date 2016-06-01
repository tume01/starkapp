from django.conf.urls import url

from . import views

app_name = 'headquarters'

urlpatterns = [    
    url(r'^hq/create', views.create_headquarters_index, name='hq/create_index'),
    url(r'^hq/create/insert', views.create_headquarters, name='hq/create_insert'),

    url(r'^hq/edit', views.update_headquarters_index, name='/hq/edit_index'),
    url(r'^hq/', views.index, name='hq/index'),
]