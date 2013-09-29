from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Organization


class OrganizationMiddleware(object):

    def process_request(self, request):
        subdomain = request.subdomain
        user = request.user

        if subdomain is None:
            request.organization = None
            return

        organization = get_object_or_404(
            Organization, slug__iexact=subdomain.lower()
        )

        if user.is_authenticated() and organization != user.organization:
            raise Http404

        request.organization = organization
