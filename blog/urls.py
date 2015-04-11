from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'browser/$', views.recipe_browser,  name='recipe_browser'),
    url(r'^(?P<slug>\S+)/$', views.DetailView.as_view(), name='detail')
)
