from django.db import models
from django.urls import *
# Create your models here.
class School(models.Model):
    scname = models.CharField(max_length=100)
    sclocation = models.CharField(max_length=100)
    scprinciple = models.CharField(max_length=100)
    
class Student(models.Model):
    scname = models.ForeignKey()
    stname = models.CharField(max_length=100)