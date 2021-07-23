from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=254, blank=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
