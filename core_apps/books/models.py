from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(_("name"), max_length=200, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        verbose_name=_("publisher"), max_length=250, unique=True
    )


class Book(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(verbose_name=_("title"), max_length=255)
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="authors",
        blank=True,
        null=True,
    )
    publisher = models.ForeignKey(
        Publisher, on_delete=models.PROTECT, blank=True, null=True
    )
    isbn13 = models.BigIntegerField(
        verbose_name=_("ISBN13"), unique=True, null=True, blank=True
    )
    for_kids = models.BooleanField(verbose_name=_("for kids"), default=False)
    textbook = models.BooleanField(verbose_name=_("textbook"), default=False)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ["author__name", "title"]

    def __str__(self):
        return f'"{self.title}" {self.author}'
