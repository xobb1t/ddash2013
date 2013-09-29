from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^openid/', include('openid_provider.urls')),
    url(r'^', include('accounts.urls')),
    url(r'^', include('organizations.private_urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
