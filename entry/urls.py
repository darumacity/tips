# coding: utf-8
from django.conf.urls import patterns, url
from entry import views

urlpatterns = patterns('',
    url(r'^$', views.top),
    url(r'^(?P<entry_id>\d+)/$', views.content, name='content'),
)
