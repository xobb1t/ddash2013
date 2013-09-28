from django.utils.functional import SimpleLazyObject

from .models import Organization


class OrganizationMiddleware(object):

    def process_request(self, request):
        def get_organization():
            try:
                return Organization.objects.get(slug=request.subdomain)
            except Organization.DoesNotExist:
                return None
        request.organization = SimpleLazyObject(get_organization)
