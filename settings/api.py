from django.conf.urls import include, url

urlpatterns = [
    url(r'^catalog/', include('catalog.api')),
]
