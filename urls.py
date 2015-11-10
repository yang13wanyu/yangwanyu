from django.conf.urls.defaults import patterns, include, url
from wan import views
# -*- coding: utf-8 -*-
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^search_form/$',views.search_form),
    (r'^search/$',views.search),
    (r'^search/search/service/$',views.service),
    (r'^search/search/delete/$',views.delete),
    
    # Examples:
    # url(r'search^$', 'ywy.views.home', name='home'),
    # url(r'^ywy/', include('ywy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
