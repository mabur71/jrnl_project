"""jrnl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog.views import blog_main, all_logs, add_log

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^dms(?P<num_station>(\d){3})/', all_logs, name='all_logs'),
    url(r'^dms797/', all_logs, {'site':'dms797'}, name='all_logs'),
    url(r'^dms774/', all_logs, {'site':'dms774'}, name='all_logs'),
    url(r'^dms726/', all_logs, {'site':'dms726'}, name='all_logs'),
    url(r'^dms_troick/', all_logs, {'site':'dms_troick'}, name='all_logs'),
    url(r'^$', blog_main, name='blog_name'),
    url(r'^add_record/', add_log),
]
