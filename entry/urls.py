# coding: utf-8
from django.conf.urls import patterns, url
from entry import views

urlpatterns = patterns('',
    url(r'^$', views.top, name='top'),
    url(r'^media/(?P<media_path>.+)/$', views.media, name='media'),
    url(r'^(?P<entry_id>\d+)/$', views.content, name='content'),
    url(r'^(?P<entry_id>\d+)/(?P<resource_path>.+)/$', views.resource),
    url(r'^tag/(?P<tag_id>\d+)/$', views.tag, name='tag'),
)
