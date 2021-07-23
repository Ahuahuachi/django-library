from django.urls import path
from .views import (
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    BookDetailView,
)

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="list"),
    path("<int:pk>/", BookDetailView.as_view(), name="detail"),
    path("new/", BookCreateView.as_view(), name="create"),
    path("edit/<int:pk>", BookUpdateView.as_view(), name="update"),
    path("delete/<int:pk>", BookDeleteView.as_view(), name="delete"),
]
