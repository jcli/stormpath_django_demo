from django.conf.urls import patterns, url

from bookmark import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^signup/$', views.user_signup, name='user_signup'),
                       url(r'^user/$', views.user_view, name='user'),
                   )
