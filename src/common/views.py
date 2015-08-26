# coding: utf-8
import requests
from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponseRedirect
from django.views import generic
from django.utils.translation import ugettext as _
from django import shortcuts
from globals import globals


class TreeResolver(generic.View):
    @classmethod
    def prepare_get(cls, f):
        def wrapper(obj, request, **kwargs):
            kwargs['session'] = request.session
            if not kwargs['path_name']:
                if hasattr(obj, 'root_view'):
                    return obj.root_view()(request, **kwargs)
                else:
                    raise Http404('Страница не найдена')

            path = kwargs['path_name'].strip('/').split('/')
            obj_id = False
            try:
                obj_id = int(path[len(path) - 1])
                path.pop()
            except:
                pass
            kwargs['obj_id'] = obj_id

            path.reverse()
            obj.tree_path = path

            try:
                obj.tree_object = obj.tree_model.objects.get(name=obj.tree_path[0])
            except obj.tree_model.DoesNotExist:
                if not kwargs['path_name'].endswith('/'):
                    return HttpResponseRedirect("%s/" % request.path)

                raise Http404('Страница не найдена')

            return f(obj, request, **kwargs)

        return wrapper


def get_seo(seoble_obj=None, add_root=None):
    config = globals.config

    stitle = sdescription = skeywords = False
    title = []
    breadcrumbs = []

    if seoble_obj:
        queue = [seoble_obj]

        if hasattr(seoble_obj, 'parent'):
            parent = seoble_obj.parent
            while parent:
                queue.append(parent)
                parent = parent.parent

        if add_root: queue.append(add_root)

        for item in queue:
            title.append(item.title)
            if not stitle: stitle = item.seo_title
            if not sdescription: sdescription = item.seo_description
            if not skeywords: skeywords = item.seo_keywords

            breadcrumbs.append({
                'title': item.title,
                'path': item.get_full_path(),
            })

    title.append(config['seo_title'])

    breadcrumbs.append({
        'title': _('Main'),
        'path': '/'
    })

    breadcrumbs.reverse()

    return {
        'title': stitle if stitle else " | ".join(title),
        'description': sdescription if sdescription else config['seo_description'],
        'keywords': skeywords if skeywords else config['seo_keywords'],
        'breadcrumbs': breadcrumbs,
    }


def get_default_context(current):
    return {
        'seo': get_seo(current),
        'current': current,
    }


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def recaptcha_verify(request, captcha):
    url = "https://www.google.com/recaptcha/api/siteverify"
    params = {
        'secret': settings.RECAPTCHA_SECRET_KEY,
        'response': captcha,
        'remoteip': get_client_ip(request)
    }

    verify_rs = requests.get(url, params=params, verify=True)
    verify_rs = verify_rs.json()
    success = verify_rs.get("success", False)
    return True if success else verify_rs.get('error-codes', None) or "Unspecified error."


def get_paginator(collection, per_page=None, page=None):
    if not page: page = globals.request.GET.get('page')
    if not per_page: per_page = globals.config['per_page']
    paginator = Paginator(collection, per_page)

    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return items


url_pattern = r'^(?P<path_name>\S*)/?$'
