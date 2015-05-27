# coding: utf-8

from django.shortcuts import render_to_response
from django.views.static import serve
from os import path
from entry.models import Tag, Entry

# Create your views here.

def media(request, media_path):
    media_root = path.join(path.abspath(path.dirname(__file__)), 'templates/entry/media')
    return serve(request, media_path, media_root)

def top(request):
    return render_to_response('entry/archive.html',
                              {'archive_info': ArchiveInfo("最近の記事",
                                                           Entry.objects.all()),
                               'sidebar_info': SidebarInfo})

def content(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    return render_to_response(entry.path, {'sidebar_info': SidebarInfo})

def resource(request, entry_id, resource_path):
    entry = Entry.objects.get(id=entry_id)
    return serve(request, resource_path, path.dirname(entry.path))

def tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    return render_to_response('entry/archive.html',
                              {'archive_info': ArchiveInfo(tag.name,
                                                           Entry.objects.filter(tags__id=tag_id)),
                               'sidebar_info': SidebarInfo})

class SidebarInfo:
    
    def __init__(self):
        self.recent_entries = Entry.objects.all()[:5]
        self.tags = Tag.objects.all()

class ArchiveInfo:

    def __init__(self, title, query):
        self.title = title
        self.entries = query
