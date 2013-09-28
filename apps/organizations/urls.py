from django.conf.urls import url, patterns
from django.views.generic import TemplateView

from .views import registration_view, check_organization_slug


urlpatterns = patterns(
    '',
    url(r'^registration/$', registration_view,
        name='organizations_registration'),
    url(r'^check-slug/$', check_organization_slug,
        name='organizations_check_slug'),
    url(r'^registration/success/$', TemplateView.as_view(
        template_name='organizations/registration_success.html',
    ), name='organizations_registration_success'),
)
