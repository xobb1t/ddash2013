from django.conf.urls import include, patterns, url

from .views import activate, login_view


urlpatterns = patterns(
    '',
    url(r'^login/$', login_view, name='accounts_login'),
    url(r'^activate/$', activate, name='accounts_activate'),
    url(r'^', include('django.contrib.auth.urls')),
)
