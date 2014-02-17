from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from phones.views import get_phone_json

admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    # Examples:
    # url(r'^$', 'angular_project.views.home', name='home'),
     url(r'^phones/get_phone_json', get_phone_json, name='get_phone_json'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
