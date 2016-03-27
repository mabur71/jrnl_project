# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# Create your views here.

def test(request, *args, **kwargs):
	return HttpResponse('Dummy view.')

def blog_main(request, *args, **kwargs):
	return  HttpResponseRedirect('dms797/')

def all_logs(request, num_station):
	dms_set = ['797', '726', '774']
	if num_station not in dms_set:
		raise Http404("Page not found")
	return render(request, 'all_logs.html', {
		'num_station' : num_station,
	})
