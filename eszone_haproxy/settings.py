"""
Django settings for eszone_haproxy project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# DEVELOPMENT (DEFAULT) SETTINGS
# Secret key for development use only !
SECRET_KEY = '&sl6qtiuk_7&ef9iwkx1r031cj-(!dx15x9+5ivuke=n6jqdaq'

# Enable debug for development
DEBUG = True

# Left this empty with DEBUG set to True
ALLOWED_HOSTS = []

# Databases configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# PRODUCTION SETTINGS
# You should run this application with ENV=production set in your production environment
if os.environ.get('ENV') == 'production':
    # Provide your secure secret key
    SECRET_KEY = 'write your secret code here'

    # Running with DEBUG enabled in production is insecure
    DEBUG = False

    # Add hosts, which will connect to this API
    ALLOWED_HOSTS = [
        '127.0.0.1',
    ]


# GENERAL SETTINGS
# Definition of used applications
INSTALLED_APPS = (
    'rest_framework',
    'api_core',
    'api_haproxy',
)

# Definition of used middleware
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

# Rest framework configuration
REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

# Path within application to main file with url setup
ROOT_URLCONF = 'eszone_haproxy.urls'

# Path to file containing wsgi configuration ready for deployment
WSGI_APPLICATION = 'eszone_haproxy.wsgi.application'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = True
USE_TZ = True


# APPLICATION SETTINGS
# API Version, used also within urls
API_VERSION_PREFIX = 'v1'