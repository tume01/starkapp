"""starkapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^products/', include('products.urls')),
    url(r'^activities/', include('activities.urls')),
    url(r'^bungalows/', include('bungalow.urls')),
    url(r'^bungalowReservations/', include('bungalow_reservation.urls')),
    url(r'^promotions/', include('promotions.urls')),
    url(r'^memberships/', include('memberships.urls')),
    url(r'^membership_application/', include('membership_application.urls')),
    url(r'^fine/', include('fine.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^eventstype/', include('events_type.urls')),
    url(r'^providers/', include('providers.urls')),    
    url(r'^servicios/', include('servicios.urls')),
    url(r'^environment/', include('environment.urls')),
    url(r'^headquarters/', include('headquarters.urls')),
    url(r'^events', include('events.urls')),
    url(r'^login/', include('login.urls')),
    url(r'^ubigeo/', include('ubigeo.urls')),
    url(r'^bungalow_service/', include('bungalow_service.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
