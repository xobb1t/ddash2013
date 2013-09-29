from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='index.html'),
        name='index'),
    url(r'^organizations/', include('organizations.urls')),
    url(r'^wtf/$', TemplateView.as_view(template_name='pages/textpage.html')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^t/(.*)$', 'django.shortcuts.render'),
    )
