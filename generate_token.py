#!/usr/bin/env python
"""
This is a helper script, which provides way to generate a first token. Generated token can be used to manage tokens with
API views contained in a api_core module. If an token authentication is enabled in a api_haproxy module,  generated
token may be used with API views provided in api_haproxy as well.
"""
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'eszone_haproxy.settings'

from api_core.models import SimpleTokenAuthModel


if __name__ == '__main__':
    token = SimpleTokenAuthModel()
    token.save()
    print token.token_uuid
