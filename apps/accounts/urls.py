from django.conf.urls import include, patterns, url

from .views import activate, login_view, set_password, profile


urlpatterns = patterns(
    '',
    url(r'^profile/(?P<slug>\w+)?$', profile, name='accounts_profile'),
    url(r'^login/$', login_view, name='accounts_login'),
    url(r'^set_password/$', set_password, name='accounts_set_password'),
    url(r'^activate/$', activate, name='accounts_activate'),
    url(r'^', include('django.contrib.auth.urls')),
)
