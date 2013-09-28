from .models import Organization


class OrganizationMiddleware(object):

    def process_request(self, request):
        try:
            self.organization = Organization.objects.get(
                slug=request.subdomain
            )
        except Organization.DoesNotExist:
            pass
