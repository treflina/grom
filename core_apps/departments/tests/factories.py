import factory

from ..models import Department


class DepartmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Department

    name = "Test Department Name"
    short_name = "TDN"
