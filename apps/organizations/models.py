from django.db import models
from django.utils.translation import ugettext_lazy as _


class Organization(models.Model):

    name = models.CharField(_(u'name'), max_length=255)
    slug = models.SlugField(_(u'slug'), max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _(u'organization')
        verbose_name_plural = _(u'organizations')
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name
