from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^organizations/', include('organizations.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^t/(.*)$', 'django.shortcuts.render'),
    )
