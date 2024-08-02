from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):

    name = models.CharField(verbose_name=_("name"), max_length=255)
    date_from = models.DateField()
    date_to = models.DateField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return f"{self.name} ({self.date_from}-{self.date_to})"
