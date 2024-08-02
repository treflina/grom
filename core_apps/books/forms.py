from autocomplete import widgets
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Author, Book


class AuthorForm(ModelForm):
    model = Author
    fields = ("name",)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = (
            "title",
            "author",
            "publisher",
            "isbn13",
            "for_kids",
            "textbook",
        )
        widgets = {
            "author": widgets.Autocomplete(
                name="author",
                options=dict(
                    multiselect=False,
                    model=Author,
                    custom_strings={
                        "no_results": _("No results"),
                        "more_results": _("More results"),
                    },
                ),
                attrs={"data-html": "hmm"},
            )
        }
