# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.

def test(request, *args, **kwargs):
	return HttpResponse('Dummy view.')

def all_logs(request):
	return render(request, 'all_logs.html') 
