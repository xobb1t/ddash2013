from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.utils import simplejson as json
from django.views.decorators.http import require_POST

from accounts.utils import send_activation_email

from .decorators import owner_required
from .forms import (
    OrganizationRegistrationForm, OwnerRegistrationForm,
    InviteForm, OrganizationForm,
)
from .models import Organization


def registration_view(request):

    user_form = OwnerRegistrationForm(data=request.POST or None,
                                      prefix='owner')
    organization_form = OrganizationRegistrationForm(
        data=request.POST or None, prefix='organization'
    )
    if user_form.is_valid() and organization_form.is_valid():
        organization = organization_form.save()
        user = user_form.save(commit=False)
        user.organization = organization
        user.is_owner = True
        user.save()

        activation = user.make_activation()
        send_activation_email(request, activation)

        return redirect('organizations_registration_success')
    return render(request, 'organizations/registration.html', {
        'organization_form': organization_form,
        'user_form': user_form
    })


@require_POST
def check_organization_slug(request):
    slug = request.POST.get('slug')
    if slug is None:
        raise Http404
    data = {
        'allowed': not Organization.objects.filter(slug__iexact=slug).exists()
    }
    return HttpResponse(json.dumps(data), mimetype='application/json')


@owner_required
def organization_detail(request):
    if not request.user.is_owner:
        raise Http404
    organization = request.organization

    invite_form = InviteForm(data=request.POST or None,
                             organization=organization,
                             prefix='invite')
    if invite_form.is_valid():
        user = invite_form.save()
        activation = user.make_activation()
        send_activation_email(request, activation)

    edit_form = OrganizationForm(data=request.POST or None,
                                 instance=organization,
                                 prefix='edit')
    if edit_form.is_valid():
        organization = edit_form.save()

    members = organization.members.all()
    return render(request, 'organizations/organization_detail.html', {
        'object_list': members,
        'organization': organization,
        'invite_form': invite_form,
        'edit_form': edit_form
    })
