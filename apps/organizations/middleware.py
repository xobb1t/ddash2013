from django.http import Http404

from .models import Organization


class OrganizationMiddleware(object):

    def process_request(self, request):
        if request.subdomain is None:
            return
        subdomain = request.subdomain
        try:
            request.organization = Organization.objects.get(
                slug__iexact=subdomain
            )
        except Organization.DoesNotExist:
            raise Http404
