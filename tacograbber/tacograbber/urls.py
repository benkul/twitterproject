from django.conf.urls import patterns, include, url
from grabber import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tacograbber.views.home', name='home'),
    # url(r'^tacograbber/', include('tacograbber.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^grabber/', include('grabber.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^twython/', include('twython_django_oauth.urls')),
    url(r'^post_tweet/$', views.create_tweet, name="create_tweet"),

)

#if settings.DEBUG:
#    urlpatterns += patterns(
#        'django.views.static',
#        (r'media/(?P<path>.*)',
#        'serve',
#        {'document_root': settings.MEDIA_ROOT}), )