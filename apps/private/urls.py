from django.conf.urls import include, patterns, url


urlpatterns = patterns(
    '',
    url(r'^openid/', include('openid_provider.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^', include('organizations.private_urls')),
)
