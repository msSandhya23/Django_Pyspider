from django.db import models

# Create your models here.
class Book(models.Model):
    bname = models.CharField(max_length=100)
    author = models.CharField(max_length=100)