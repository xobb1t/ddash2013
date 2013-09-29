import hashlib
import random

from datetime import timedelta

from django.conf import settings
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.utils import timezone


class ActivationManager(models.Manager):

    def make_activation(self, user):
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        base = user.email
        if isinstance(base, unicode):
            base = base.encode('utf-8')
        key = hashlib.sha1(salt+base).hexdigest()
        expires_at = timezone.now() + timedelta(
            days=getattr(settings, 'ACTIVATION_DAYS', 7)
        )
        return self.create(user=user, key=key, expires_at=expires_at)

    def activate(self, key):
        try:
            activation = self.get(
                key=key, is_activated=False, expires_at__gte=timezone.now()
            )
        except self.model.DoesNotExist:
            return False
        activation.is_activated = True
        activation.save()
        user = activation.user
        user.is_active = True
        user.save()
        return user


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_superuser, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email, is_superuser=is_superuser, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)
