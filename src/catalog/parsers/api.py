# coding: utf-8

from urllib2 import urlopen
from django.conf.urls import include, url
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def get_xml_request(request, url_request):
    content = urlopen(url_request)
    return HttpResponse(content.read(), content_type='text/xml')

urlpatterns = [
    url(r'^getxml_by_url/(.+)', get_xml_request),
]
