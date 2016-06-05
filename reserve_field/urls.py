from django.conf.urls import url
from . import views

app_name = 'reserve_field'

urlpatterns = [
    url(r'^', views.index, name='index'),
]