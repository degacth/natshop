from django.conf.urls import url
from common.views import url_pattern
from . import views

urlpatterns = [
    url(url_pattern, views.SectionResolver.as_view()),
]
