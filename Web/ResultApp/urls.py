from django.conf.urls import patterns, url
from ResultApp import views
urlpatterns = patterns('',
    url(r'^$', views.Index, name='index'),  
   
)

