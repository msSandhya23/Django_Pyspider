from django.db import models

# Create your models here.
class School(models.Model):
    Scname = models.CharField(max_length=100,unique=True)
    ScLocation = models.CharField(max_length=100)
    #ScPrinciple  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.scname
class Student(models.Model):
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    def __str__(self):
        return self.name