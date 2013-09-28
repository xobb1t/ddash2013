from django.conf.urls import include, patterns, url
from .views import member_list, invite_member


urlpatterns = patterns(
    '',
    url(r'^openid/', include('openid_provider.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^members/$', member_list, name='private_member_list'),
    url(r'^members/invite/$', invite_member, name='private_member_invite'),
)
