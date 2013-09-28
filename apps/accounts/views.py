from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .models import Activation
from .forms import LoginForm


def activate(request):
    key = request.GET.get('key', '')
    user = Activation.objects.activate(key)
    if not user:
        raise Http404
    user.backend = 'accounts.activate'
    login(request, user)
    if not user.has_usable_password():
        redirect('accounts_new_password')
    return render(request, 'accounts/activation_success.html')


def login_view(request):
    form = LoginForm(request.POST or None, organization=request.organization)
    if form.is_valid():
        login(request, form.user_cache)
        next = request.GET.get('next')
        return redirect(next or settings.LOGIN_REDIRECT_URL)
    return render(request, 'private/login.html', {
        'form': form
    })
