# coding: utf-8
from django.http import HttpResponse

# Create your views here.

def top(request):
    return HttpResponse('エントリーのトップ画面')
