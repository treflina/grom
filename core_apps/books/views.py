from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import AuthorForm, BookForm
from .models import Author, Book


class AuthorCreateView(CreateView):

    model = Author
    form_class = AuthorForm


class BookCreateView(CreateView):

    model = Book
    form_class = BookForm
    success_url = reverse_lazy("book:add_book")
