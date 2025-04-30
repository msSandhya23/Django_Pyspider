from django.db import models
from django.contrib import admin
# Create your models here.
class School(models.Model):
    scname = models.CharField(max_length=100)
    scaddress = models.CharField(max_length=255)
    
class Student(models.Model):
    scname = models.ForeignKey(School,on_delete=models.CASCADE)
    stname = models.CharField(max_length=100)
    stage = models.IntegerField()