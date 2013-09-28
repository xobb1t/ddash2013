from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.utils import simplejson as json

from .forms import RegistrationForm, OwnerRegistrationForm


def registration_view(request):

    user_form = OwnerRegistrationForm(data=request.POST or None,
                                      prefix='owner')
    organization_form = RegistrationForm(data=request.POST or None,
                                         prefix='organization')
    if user_form.is_valid() and organization_form.is_valid():
        organization = organization_form.save()
        user = user_form.save(commit=False)
        user.organization = organization
        user.is_owner = True
        user.save()
        return redirect('organizations_registration_success')
    return render(request, 'organizations/registration.html', {
        'organization_form': organization_form,
        'user_form': user_form
    })


def check_organization_slug(request):

    slug = request.POST.get('slug')
    if slug is None:
        raise Http404
    data = {
        'allowed': not Organization.objects.filter(slug=slug).exists()
    }
    return HttpResponse(json.dumps(data), mimetype='application/json')
