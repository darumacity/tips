# coding: utf-8
from django.conf.urls import patterns, url
from entry_admin import views

urlpatterns = patterns('',
    url(r'^$', views.top, name="entry_admin"),
)
