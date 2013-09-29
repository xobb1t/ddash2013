from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = patterns(
    '',
    url(r'^openid/', include('openid_provider.urls')),
    url(r'^wtf/$', TemplateView.as_view(template_name='pages/textpage.html')),
    url(r'^', include('accounts.urls')),
    url(r'^', include('organizations.private_urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
