# coding: utf-8

from django.shortcuts import render_to_response
from entry.models import Entry

# Create your views here.

def top(request):
    entries = Entry.objects.all()
    return render_to_response('entry/top.html', {'entries': entries})

def content(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    return render_to_response(entry.path)

def resource(request, entry_id, resource_path):
    from django.views.static import serve
    from os import path

    entry = Entry.objects.get(id=entry_id)
    return serve(request, resource_path, path.dirname(entry.path))
