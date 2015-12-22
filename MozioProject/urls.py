from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'app.views.firstpage', name='firstpage'),
    url(r'^home$', 'app.views.firstpage', name='firstpage'),
    url(r'^firstpage$', 'app.views.firstpage', name='firstpage'),
    url(r'^secondpage$', 'app.views.secondpage', name='secondpage'),
    url(r'^savecoordinates', 'app.views.savecoordinates', name='savecoordinates'),
    url(r'^getcoordinates/(?P<id>\d+)$', 'app.views.getcoordinates', name='getcoordinates'),
)
