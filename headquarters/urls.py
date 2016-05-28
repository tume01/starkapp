from django.conf.urls import url

from . import views

app_name = 'headquarters'

urlpatterns = [
    url(r'^$', views.index, name='index'),
]