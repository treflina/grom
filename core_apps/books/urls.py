from django.urls import path

from .views import AuthorCreateView, BookCreateView

app_name = "books"

urlpatterns = [
    path("ksiazki/dodaj/", BookCreateView.as_view(), name="add_book"),
    path("autorzy/dodaj/", AuthorCreateView.as_view(), name="add_author"),
]
