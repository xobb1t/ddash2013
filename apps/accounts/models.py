from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from openid_provider.models import OpenID

from .managers import UserManager, ActivationManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_(u'email'), max_length=255, unique=True)

    full_name = models.CharField(_(u'full name'), max_length=255)
    login = models.SlugField(_(u'login'), max_length=255)
    organization = models.ForeignKey('organizations.Organization',
                                     related_name='members')
    is_owner = models.BooleanField(_(u'is owner'), default=False)
    is_active = models.BooleanField(_(u'is active'), default=False)
    joined_at = models.DateTimeField(_(u'joined at'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['login']

    objects = UserManager()

    class Meta:
        verbose_name = _(u'user')
        verbose_name_plural = _(u'users')
        unique_together = ['organization', 'login']

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.login

    def make_activation(self):
        if self.is_active:
            return
        return self.activations.make_activation(self)


class Activation(models.Model):

    user = models.ForeignKey(User, related_name='activations')
    key = models.CharField(max_length=40)
    is_activated = models.BooleanField(default=False)
    expires_at = models.DateTimeField()

    objects = ActivationManager()

    def is_expired(self):
        return timezone.now() > self.expires_at


def create_openid_on_user_create(sender, instance, created, **kwargs):
    if created:
        OpenID.objects.get_or_create(user=instance, defaults={
            'default': True, 'openid': instance.login
        })

post_save.connect(create_openid_on_user_create, sender=User)
