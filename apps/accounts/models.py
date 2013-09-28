from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_(u'email'), max_length=255, unique=True)

    full_name = models.CharField(_(u'full name'), max_length=255)
    login = models.SlugField(_(u'login'), max_length=255)
    organization = models.ForeignKey('organizations.Organization')
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
