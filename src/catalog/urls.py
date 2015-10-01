from django.conf.urls import url
from django.views.generic import TemplateView
from common.views import url_pattern
from . import views

urlpatterns = [
    url('yamarket', views.Yamarket.as_view(), name="yamarket"),
    url(url_pattern, views.CatalogResolver.as_view()),
]
