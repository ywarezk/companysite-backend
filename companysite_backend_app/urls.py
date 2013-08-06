'''
our server urls are defined in this page
Created on Jun 20, 2013

@author: Yariv Katz
@version: 1.0
@copyright: nerdeez.com
'''

#===============================================================================
# begin imports
#===============================================================================

from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from companysite_backend_app.company_api.api import *
import companysite_backend_app.views

#===============================================================================
# end imports
#===============================================================================

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()

#register rest urls
v1_api = Api(api_name='v1')
v1_api.register(FlatpageResource())
v1_api.register(UtilitiesResource())
v1_api.register(GalleryResource())
v1_api.register(WorkersResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'companysite_backend_app.views.home', name='home'),
    # url(r'^companysite_backend_app/', include('companysite_backend_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    #grappelli
    (r'^grappelli/', include('grappelli.urls')),
    
    #urls for tastypie
    (r'^api/', include(v1_api.urls)),
    
    #urls for the cross domain comunications
    ('^$', companysite_backend_app.views.porthole),
    ('^proxy/', companysite_backend_app.views.proxy),
)
