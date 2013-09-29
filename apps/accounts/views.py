from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404

from .models import Activation, User
from .forms import LoginForm


def activate(request):
    key = request.GET.get('key', '')
    user = Activation.objects.activate(key)
    if not user:
        raise Http404
    user.backend = 'accounts.backends.UserAuthenticationBackend'
    login(request, user)
    if not user.has_usable_password():
        return redirect('accounts_set_password')
    return redirect('accounts_profile')


def login_view(request):
    form = LoginForm(
        data=request.POST or None,
        organization=request.organization
    )
    if form.is_valid():
        login(request, form.user_cache)
        next = request.GET.get('next')
        return redirect(next or '/')
    return render(request, 'accounts/login.html', {
        'form': form
    })


@login_required
def set_password(request):
    if request.user.has_usable_password():
        raise Http404
    form = SetPasswordForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'accounts/set_password.html', {
        'form': form
    })


@login_required
def profile(request, slug=None):
    user = request.user
    organization = request.organization
    if slug:
        if not (user.is_owner and user.organization == organization):
            raise Http404
        members = organization.members.all()
        user = get_object_or_404(members, login=slug)
    return render(request, 'accounts/profile.html', {
        'user': user,
        'organization': organization
    })
