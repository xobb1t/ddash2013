from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

from .models import User


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        self.organization = kwargs.pop('organization')
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(
                email=username,
                password=password,
                organization=self.organization
            )
            if self.user_cache is None:
                raise forms.ValidationError('Invalid email or password.')
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
