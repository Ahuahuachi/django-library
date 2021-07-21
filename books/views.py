from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Author, Book


class BookListView(ListView):
    template_name = "books/list.html"
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        authors = Author.objects.all()

        context["authors"] = authors
        return context


class BookDetailView(DetailView):
    template_name = "books/details.html"
    model = Book


class CreateBookTemplateView(TemplateView):
    template_name = "books/create.html"


class DeleteBookTemplateView(TemplateView):
    template_name = "books/delete.html"