from django.conf.urls import include, patterns, url

urlpatterns = patterns(
    '',
    url(r'^openid/', include('openid_provider.urls')),
)
