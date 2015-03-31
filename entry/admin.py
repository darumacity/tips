# coding: utf-8

from django.contrib import admin
from entry.models import Tag, Entry

# Register your models here.

admin.site.register(Tag)
admin.site.register(Entry)
