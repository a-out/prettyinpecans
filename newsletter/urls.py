from django.conf.urls import patterns, url

from newsletter import views

urlpatterns = patterns('',
    url(r'subscribe/$', views.subscribe, name='newsletter_subscribe')
)
