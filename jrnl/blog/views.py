# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Records

import logging
logger = logging.getLogger(__name__)

# Create your views here.

def test(request, *args, **kwargs):
	return HttpResponse('Dummy view.')

def blog_main(request, *args, **kwargs):
	return  HttpResponseRedirect('dms797/')

def all_logs(request, site):
	#logger.debug("view:all_logs - debug Ok!")
	site_set = ['dms797', 'dms726', 'dms774']
	if site not in site_set:
		raise Http404("Page not found")
	return render(request, 'all_logs.html', {
		'site' : site,
	})
