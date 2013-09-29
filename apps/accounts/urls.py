from django.conf.urls import include, patterns, url

from .views import (
    activate, login_view, set_password, user_detail, user_edit,
    user_delete
)


urlpatterns = patterns(
    '',
    url(r'^$', user_detail, name='accounts_user_detail'),
    url(r'^user/(?P<slug>\w+)/$', user_detail,
        name='accounts_user_detail_for_slug'),
    url(r'^user/(?P<slug>\w+)/edit/$', user_edit, name='accounts_user_edit'),
    url(r'^user/(?P<slug>\w+)/delete/$', user_delete,
        name='accounts_user_delete'),
    url(r'^login/$', login_view, name='accounts_login'),
    url(r'^set_password/$', set_password, name='accounts_set_password'),
    url(r'^activate/$', activate, name='accounts_activate'),
    url(r'^', include('django.contrib.auth.urls')),
)
