from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView, TemplateView
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


class BookCreateView(CreateView):
    template_name = "books/create.html"
    model = Book
    fields = (
        "title",
        "author",
        "publishing_year",
        "publishing_house",
        "pages",
    )


class DeleteBookTemplateView(TemplateView):
    template_name = "books/delete.html"