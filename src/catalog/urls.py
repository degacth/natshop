from django.conf.urls import url
from . import views
from common.views import url_pattern

urlpatterns = [
    url(url_pattern, views.CatalogResolver.as_view()),
]
