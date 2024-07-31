from django.contrib.auth.models import AbstractUser
from django.db import models  # noqa
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """User model."""

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
