from django.shortcuts import render
from django.views.generic import TemplateView


class ListBooksTemplateView(TemplateView):
    template_name = "books/list.html"


class BookDetailsTemplateView(TemplateView):
    template_name = "books/details.html"


class CreateBookTemplateView(TemplateView):
    template_name = "books/create.html"


class DeleteBookTemplateView(TemplateView):
    template_name = "books/delete.html"