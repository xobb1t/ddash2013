from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404

from .models import Activation
from .forms import LoginForm, UserEditForm


def activate(request):
    key = request.GET.get('key', '')
    user = Activation.objects.activate(key)
    if not user:
        raise Http404
    user.backend = 'accounts.backends.UserAuthenticationBackend'
    login(request, user)
    if not user.has_usable_password():
        return redirect('accounts_set_password')
    return redirect('accounts_user_detail')


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
def user_detail(request, slug=None):
    user = request.user
    organization = request.organization
    password_change_form = PasswordChangeForm(user, request.POST or None)

    if slug:
        if not user.is_owner:
            raise Http404
        user = get_object_or_404(organization.members.all(), login=slug)
        if not user.is_owner:
            password_change_form = SetPasswordForm(user, request.POST or None)

    if password_change_form.is_valid():
        password_change_form.save()

    return render(request, 'accounts/user_detail.html', {
        'user': user,
        'organization': organization,
        'password_change_form': password_change_form
    })


@login_required
def user_edit(request, slug=None):
    user = request.user
    organization = request.organization
    if slug:
        if not user.is_owner:
            raise Http404
        user = get_object_or_404(organization.members.all(), login=slug)

    form = UserEditForm(request.POST or None, instance=user)
    if form.is_valid():
       form.save()

    return render(request, 'accounts/user_edit.html', {
        'form': form,
        'user': user
    })


