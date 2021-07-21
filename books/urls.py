from django.urls import path
from .views import (
    BookListView,
    CreateBookTemplateView,
    DeleteBookTemplateView,
    BookDetailView,
)

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="list"),
    path("<int:pk>/", BookDetailView.as_view(), name="detail"),
    path("new/", CreateBookTemplateView.as_view(), name="create"),
    path("delete/", DeleteBookTemplateView.as_view(), name="delete"),
]
