from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeUserStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        on_delete=models.PROTECT,
        null=True,
    )

    class Meta:
        abstract = True
