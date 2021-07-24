from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import (
    DetailView,
    DeleteView,
    CreateView,
    ListView,
    TemplateView,
    UpdateView,
)
from .models import Author, Book


class BookListView(ListView):
    template_name = "books/list.html"
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        authors = Author.objects.all()

        context["authors"] = authors
        return context


class BookDetailView(PermissionRequiredMixin, DetailView):
    permission_required = "books.view_book"
    template_name = "books/details.html"
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"

    template_name = "books/create.html"
    model = Book
    fields = (
        "title",
        "author",
        "publishing_year",
        "publishing_house",
        "pages",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_pk"] = self.get_form().instance.pk

        if self.request.user.employee_information.is_rh:
            context["classified_info"] = "Informacion clasificada"

        return context


class BookUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = "books.change_book"
    template_name = "books/create.html"
    model = Book
    fields = (
        "title",
        "author",
        "publishing_year",
        "publishing_house",
        "pages",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book_pk"] = self.get_form().instance.pk
        return context


class BookDeleteView(DeleteView):
    template_name = "books/delete.html"
    model = Book
    success_url = "/books/"