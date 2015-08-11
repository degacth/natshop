from django.conf.urls import include, url
from .views import DefaultView

urlpatterns = (
    url(r'^$', DefaultView.as_view(), name='default'),
)
