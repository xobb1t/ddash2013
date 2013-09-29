from django.http import Http404

from .models import Organization


class OrganizationMiddleware(object):

    def process_request(self, request):
        if request.subdomain is None:
            request.organization = None
            return
        subdomain = request.subdomain

        try:
            organization = Organization.objects.get(
                slug__iexact=subdomain
            )
        except Organization.DoesNotExist:
            raise Http404

        user = request.user
        if user.is_authenticated() and organization != user.organization:
            raise Http404

        request.organization = organization
