from django.conf.urls import patterns, url
from grabber import views


urlpatterns = patterns('',
                    url(r'^$', views.index, name='index'),
                    url(r'^about/$', views.about, name='about'),
                    url(r'^generate/$', views.generate, name='generate'),
                    url(r'^about/(?P<bot_name>\w+)/$', views.bot_profile, name='bot_profile'),


)
