# coding: utf-8
from django.shortcuts import render 
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def top(request):
    return render(request, 'entry_admin/top.djhtml')
