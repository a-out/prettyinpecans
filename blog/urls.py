from django.conf.urls import patterns, url

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

from blog import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'posts/$', views.IndexView.as_view(), name='index'),
    url(r'posts/food/$', views.FoodIndexView.as_view(),  name='food_index'),
    url(r'posts/fashion/$', views.FashionIndexView.as_view(),  name='fashion_index'),
    url(r'posts/travel/$', views.TravelIndexView.as_view(), name='travel_index'),
    url(r'recipebrowser/$', views.recipe_browser,  name='recipe_browser'),
    url(r'^posts/(?P<slug>\S+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^search/', SearchView(
        template='search/results.html',
        searchqueryset=SearchQuerySet()
    ), name='haystack_search'),
)
