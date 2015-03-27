# coding: utf-8
from django.conf.urls import patterns, url
from entry import views

urlpatterns = patterns('',
    url(r'^$', views.top),
)
