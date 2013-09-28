from django import forms
from django.utils.translation import ugettext_lazy as _

from accounts.models import User
from .models import Organization


class RegistrationForm(forms.ModelForm):

    class Meta:
        model = Organization


class OwnerRegistrationForm(forms.ModelForm):

    password1 = forms.CharField(
        label=_(u'Password'), widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label=_(u'Password confirmation'), widget=forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ['email', 'full_name', 'login']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                _(u"The two password fields didn't match.")
            )
        return password2

    def save(self, commit=True):
        user = super(OwnerRegistrationForm, self).save(commit=commit)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user
