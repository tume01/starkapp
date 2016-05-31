from django.conf.urls import url

from . import views

app_name = 'headquarters'

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^create', views.create_headquarters, name='new'),
    #url(r'^update/(?P<headquarter_id>[0-9]+)', views.update, name='edit'),
    #TEMP
    url(r'^', views.update, name='edit'),
]