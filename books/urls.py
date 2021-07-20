from django.urls import path
from .views import BookListView, CreateBookTemplateView, DeleteBookTemplateView

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="list"),
    path("new/", CreateBookTemplateView.as_view(), name="create"),
    path("delete/", DeleteBookTemplateView.as_view(), name="delete"),
]
