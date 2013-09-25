from django.conf.urls import patterns, url
from ResultApp import views
urlpatterns = patterns('',
    url(r'^$', views.Index, name='index'),  
    url(r'menu/$', views.LeftMenu, name='menu'), 
    url(r'context/$', views.Context, name='context'), 
)

