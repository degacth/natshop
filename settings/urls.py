# coding: utf-8
"""intercater URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from catalog.models import Catalog
from config.models import init_config

config = init_config()
settings.GRAPPELLI_ADMIN_TITLE = settings.SITE_NAME = config['site_name']

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^%s' % settings.ADMIN_URL, include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^mailer/', include('mailer.urls')),
    url(r'^customer/', include('customer.urls', namespace="customer")),
    url(r'^%s/' % settings.API_URL.strip('/'), include('settings.api')),
    url(r'^%s/' % Catalog.full_path_prefix.strip('/'), include('catalog.urls')),
    url(r'^/?', include('section.urls', namespace="section")),
]
