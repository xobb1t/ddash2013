from django.conf.urls import patterns, url
from .views import organization_detail


urlpatterns = patterns(
    '',
    url(r'^organization/$', organization_detail,
        name='organizations_organization_detail'),
)
