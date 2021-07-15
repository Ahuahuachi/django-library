from django.urls import path
from .views import (
    IndexTemplateView,
    ListBooksTemplateView,
    CreateBookTemplateView,
    DeleteBookTemplateView,
)


urlpatterns = [
    path("", IndexTemplateView.as_view(), name="home"),
    path("books/", ListBooksTemplateView.as_view(), name="list_books"),
    path("new_book/", CreateBookTemplateView.as_view(), name="create_book"),
    path("delete_book/", DeleteBookTemplateView.as_view(), name="delete_book"),
]
