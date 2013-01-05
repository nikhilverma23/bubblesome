from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    'bubblesome.upload.views',
    
    url(r'^demo/$', 'demo_upload', name='demo-upload'),
   

)