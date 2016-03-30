# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Records, Sites

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
	sites = Sites.objects.filter()
	records = Records.objects.filter(site__name = site)
	limit = 10
	page = request.GET.get('page', 1)
	paginator = Paginator(records, limit)
	paginator.baseurl = '/' + site + '/?page='
	page = paginator.page(page)
	return render(request, 'all_logs.html', {
		'sites': sites,
		'cur_site': site,
		'records': page.object_list,
		'paginator': paginator,
		'page': page,
		'debug': '',
	})
