# Django settings for project project.
import os

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')
PROJECT_ROOT = os.path.normpath(os.path.abspath(PROJECT_ROOT))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Dima Kukushkin', 'dima@kukushkin.me'),
    ('Tima Kukushkin', 'tima@kukushkin.me'),
    ('Alex Trolev', 'trolev@gmail.com'),
)

MANAGERS = ADMINS
ALLOWED_HOSTS = ['*']
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'public', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'public', 'static')
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = 'v)d_ljcd-uv65=kti4=$&ynfu-ckay7xh=i^ob8t&=3e0@r2@7'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'sitesutils.middleware.RequestSiteMiddleware',

    'organizations.middleware.OrganizationMiddleware',
)

ROOT_URLCONF = 'project.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'project.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'sitesutils.context_processors.site',
    'organizations.context_processors.organization',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_gears',
    'easy_thumbnails',
    'gravatar',
    'openid_provider',
    'sitesutils',
    'south',
    'subdomains',
    'widget_tweaks',

    'accounts',
    'organizations',
    'private',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


AUTH_USER_MODEL = 'accounts.User'

SUBDOMAIN_URLCONFS = (
    (r'^www$', 'project.urls'),
    (r'^(\w+)$', 'private.urls'),
)

GEARS_ROOT = os.path.join(PROJECT_ROOT, 'static')
GEARS_DIRS = (
    os.path.join(PROJECT_ROOT, 'assets'),
)
GEARS_COMPRESSORS = {
    'text/css': 'gears_clean_css.CleanCSSCompressor',
    'application/javascript': 'gears_uglifyjs.UglifyJSCompressor',
}
GEARS_COMPILERS = {
    '.less': 'gears_less.LESSCompiler',
}

GEARS_PUBLIC_ASSETS = (
    lambda path: not any(path.endswith(ext) for ext in ('.css', '.js')),
    lambda path: path.startswith('js/libs'),
    r'^css/style\.css$',
    r'^js/script\.js$',
)

AUTHENTICATION_BACKENDS = (
    'accounts.backends.UserAuthenticationBackend',
)

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

