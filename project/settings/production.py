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
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'noreply@singlepointhq.com'
DEFAULT_FROM_EMAIL = 'noreply@singlepointhq.com'
EMAIL_PORT = 25

ALLOWED_HOSTS = ['.singlepointhq.com']


BROKER_URL = 'redis://localhost:6379/0'
INSTALLED_APPS += ("djcelery", "djcelery_email",)
EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend'
CELERYD_CONCURRENCY = 2
CELERYD_MAX_TASKS_PER_CHILD = 100
