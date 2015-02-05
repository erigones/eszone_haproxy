from django.conf.urls import include, url
from settings import API_VERSION_PREFIX

urlpatterns = [
    url(r'^{0}/'.format(API_VERSION_PREFIX), include('api_core.urls')),
    url(r'^{0}/haproxy/'.format(API_VERSION_PREFIX), include('api_haproxy.urls'))
]
