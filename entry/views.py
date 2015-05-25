# coding: utf-8

from django.shortcuts import render_to_response
from entry.models import Tag, Entry

# Create your views here.

def media(request, media_path):
    from django.views.static import serve
    from os import path

    media_root = path.join(path.abspath(path.dirname(__file__)), 'templates/entry/media')
    return serve(request, media_path, media_root)

def top(request):
    return render_to_response('entry/archive.html',
                              {'archive_title': "最近の記事",
                               'entries': Entry.objects.all(),
                               'recent_entries': Entry.objects.all(),
                               'tags': Tag.objects.all()})

def content(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    return render_to_response(entry.path, {'recent_entries': Entry.objects.all(),
                                           'tags': Tag.objects.all()})

def resource(request, entry_id, resource_path):
    from django.views.static import serve
    from os import path

    entry = Entry.objects.get(id=entry_id)
    return serve(request, resource_path, path.dirname(entry.path))

def tag(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    return render_to_response('entry/archive.html',
                              {'archive_title': tag.name,
                               'entries': Entry.objects.filter(tags__id=tag_id),
                               'recent_entries': Entry.objects.all(),
                               'tags': Tag.objects.all()})
