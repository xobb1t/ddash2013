from django.contrib.auth.decorators import user_passes_test
from django.http import Http404
from django.shortcuts import redirect, render

from accounts.utils import send_activation_email

from accounts.forms import InviteForm


owner_required = user_passes_test(
    lambda u: u.is_authenticated() and u.is_owner
)


@owner_required
def member_list(request):
    if not request.user.is_owner:
        raise Http404
    organization = request.organization
    qs = organization.members.all()
    return render(request, 'private/ornigazation_members.html', {
        'object_list': qs
    })


@owner_required
def invite_member(request):
    form = InviteForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_unusable_password()
        user.organization = request.organization
        user.save()
        activation = user.make_activation()
        send_activation_email(request, activation)
        return redirect('private_member_list')
    return render(request, 'private/invite_member.html', {
        'form': form
    })
