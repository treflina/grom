from autocomplete import widgets
from django.forms import ModelForm

from core_apps.books.models import Book
from core_apps.departments.models import Department

from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["book", "department", "project", "novelty"]
        widgets = {
            "book": widgets.Autocomplete(
                name="book", options=dict(multiselect=False, model=Book)
            ),
            "department": widgets.Autocomplete(
                name="department",
                options=dict(multiselect=False, model=Department),
            ),
        }
