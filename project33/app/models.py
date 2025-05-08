from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,unique=True)
    age = models.IntegerField()
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.name