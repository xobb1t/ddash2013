from django.conf.urls import patterns, url
from .views import organization_detail, organization_edit


urlpatterns = patterns(
    '',
    url(r'^organization/$', organization_detail,
        name='organizations_organization_detail'),
    url(r'^organization/edit/$', organization_edit,
        name='organizations_organization_edit'),
)
