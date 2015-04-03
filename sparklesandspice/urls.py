from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', include('blog.urls')),
    url(r'^posts/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  {
        'document_root': settings.MEDIA_ROOT,
    }),
    url(r'^admin/', include(admin.site.urls)),
)
