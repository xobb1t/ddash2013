from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, organization=request.organization)
        if form.is_valid():
            login(request, form.user_cache)
            next = request.GET.get('next')
            return redirect(next or settings.LOGIN_REDIRECT_URL)
    else:
        form = LoginForm(organization=request.organization)
    return render(request, 'private/login.html', {
        'form': form
    })
