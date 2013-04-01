from django.conf.urls import patterns, url

from bookmark import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^signin/$', views.user_signin, name="user_signin"),
                       url(r'^signup/$', views.user_signup, name='user_signup'),
                       url(r'^signout/$', views.user_signout, name='user_signout'),
                       url(r'^save/$', views.user_save, name='user_save'),
                   )

