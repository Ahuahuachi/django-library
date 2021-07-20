from django.contrib import admin
from django.db.models import ManyToManyField
from django.forms.widgets import CheckboxSelectMultiple
from .models import Author, Book, PublishingHouse


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ("author",)
    list_display = ("title", "publishing_year")


@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
