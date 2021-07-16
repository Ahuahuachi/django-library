from django.urls import path
from .views import ListBooksTemplateView, CreateBookTemplateView, DeleteBookTemplateView

app_name = "books"

urlpatterns = [
    path("", ListBooksTemplateView.as_view(), name="list"),
    path("new/", CreateBookTemplateView.as_view(), name="create"),
    path("delete/", DeleteBookTemplateView.as_view(), name="delete"),
]
