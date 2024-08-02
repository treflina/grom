from django.db import models
from django.utils.translation import gettext_lazy as _

from core_apps.books.models import Book
from core_apps.common.models import TimeUserStampedModel
from core_apps.departments.models import Department
from core_apps.projects.models import Project


class Order(TimeUserStampedModel):
    class OrderStatus(models.TextChoices):
        PLACED = "placed", _("placed")
        PROCESSING = "processing", _("processing")
        CATALOGING = "cataloging", _("cataloging")
        FULFILLED = "fulfilled", _("fulfilled")

    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    novelty = models.BooleanField(verbose_name=_("novelty"), default=False)
    project = models.ForeignKey(
        Project, on_delete=models.PROTECT, null=True, blank=True
    )
    status = models.CharField(max_length=15, default=OrderStatus.PLACED)
    price = models.DecimalField(
        verbose_name=_("price"), decimal_places=2, max_digits=7, default=0
    )
    amount = models.PositiveSmallIntegerField(
        verbose_name=_("amount"), default=1
    )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

    def __str__(self):
        order_date = self.created_at.strftime("%d.%m/%y")
        return f"{order_date} {self.department.short_name} - {self.book.title}"
