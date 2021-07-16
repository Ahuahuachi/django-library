from django.db import models

# Create your models here.


class PublishingHouseModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class BookModel(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(to=AuthorModel)
    publishing_year = models.DateField()
    publishing_house = models.ForeignKey(
        to=PublishingHouseModel, on_delete=models.PROTECT
    )
    pages = models.IntegerField()
