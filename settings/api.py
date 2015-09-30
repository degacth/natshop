from django.conf.urls import include, url

urlpatterns = [
    url(r'^catalog/', include('catalog.api')),
    url(r'^parsers/', include('catalog.parsers.api')),
    url(r'^customer/', include('customer.api')),
    url(r'^feedback/', include('feedback.api')),
]
