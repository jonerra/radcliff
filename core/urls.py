from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^player_registration/$', PlayerRegistration.as_view(), name='player_registration'),
    url('^success/$', Success.as_view(), name='success'),
)