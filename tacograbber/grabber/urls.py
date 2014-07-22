from django.conf.urls import patterns, url
from grabber import views


urlpatterns = patterns('',
                    url(r'^$', views.index, name='index'),
                    url(r'^about/$', views.about, name='about'),
                    url(r'^generate/$', views.generate, name='generate'),
                    url(r'^about/(?P<bot_name>\w+)/$', views.bot_profile, name='bot_profile'),
                    url(r'^generate/?$', views.get_tokens, name="twitter_return"),
                    url(r'^thanks/?$', views.thanks, name="twitter_callback"),


)
