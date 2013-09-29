from django.template import Library

from ..forms import (
    OrganizationForm, OrganizationRegistrationForm, OwnerRegistrationForm
)


register = Library()


@register.inclusion_tag('organizations/tags/organization_edit_form.html',
                        takes_context=True)
def organization_edit_form(context):
    organization = context.get('organization')
    return {
        'form': OrganizationForm(instance=organization)
    }


@register.inclusion_tag('organizations/registration.html')
def registration_form():
    return {
        'organization_form': OrganizationRegistrationForm(
            prefix='organization'),
        'user_form': OwnerRegistrationForm(prefix='owner'),
    }
