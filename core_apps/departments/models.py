from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):

    name = models.CharField(verbose_name=_("Department"), max_length=50)
    short_name = models.CharField(verbose_name=_("Short name"), max_length=12)

    class Meta:
        verbose_name = _("Department")
        verbose_name_plural = _("Departments")

    def __str__(self):
        return self.name
