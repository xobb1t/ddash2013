from django.conf.urls import url, patterns
from django.views.generic import TemplateView

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.member_list,
        name='organizations_member_list'),
    url(r'^edit/$', views.member_list,
        name='organizations_organization_edit'),
    url(r'^registration/$', views.registration_view,
        name='organizations_registration'),
    url(r'^check-slug/$', views.check_organization_slug,
        name='organizations_check_slug'),
    url(r'^registration/success/$', TemplateView.as_view(
        template_name='organizations/registration_success.html',
    ), name='organizations_registration_success'),
)
