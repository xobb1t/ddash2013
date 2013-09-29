import os
from .common import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'singlepoint',
    }
}

PUBLIC_ROOT = os.path.join(os.sep, 'var', 'www', 'singlepoint', 'public')
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

PREPEND_WWW = False

EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')
if EMAIL_HOST_PASSWORD:
    EMAIL_HOST = 'smtp.yandex.ru'
    EMAIL_PORT = 465
    EMAIL_HOST_USER = 'noreply@singlepointhq.com'
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'noreply@singlepointhq.com'
