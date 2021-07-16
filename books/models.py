from django.db import models

# Create your models here.


class PublishingHouse(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(to=Author)
    publishing_year = models.DateField()
    publishing_house = models.ForeignKey(to=PublishingHouse, on_delete=models.PROTECT)
    pages = models.IntegerField()
