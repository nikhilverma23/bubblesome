from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from bubblesome.settings import MEDIA_ROOT, STATIC_ROOT
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bubblesome.views.home', name='home'),
    url(r'^$', direct_to_template, {'template': 'homepage.html'}, 'homepage'),
    url(r'^upload/', include('bubblesome.upload.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
      # Static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),

)
