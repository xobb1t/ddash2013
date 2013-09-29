from django.template import Library
from ..forms import OrganizationForm

register = Library()


@register.inclusion_tag('organizations/tags/organization_edit_form.html',
                        takes_context=True)
def organization_edit_form(context):
    organization = context.get('organization')
    return {
        'form': OrganizationForm(instance=organization)
    }
