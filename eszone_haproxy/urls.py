from django.conf.urls import include, url
from settings import API_VERSION

urlpatterns = [
    url(r'^{0}/'.format(API_VERSION), include('api_core.urls')),
]
