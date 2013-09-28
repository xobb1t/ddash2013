from django.http import Http404

from .models import Organization


class OrganizationMiddleware(object):

    def process_request(self, request):
        try:
            request.organization = Organization.objects.get(
                slug__iexact=request.subdomain
            )
        except Organization.DoesNotExist:
            raise Http404
