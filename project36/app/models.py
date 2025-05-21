from django.db import models

# Create your models here.
class Emp(models.Model):
    ename = models.CharField(max_length=100)
    empno = models.IntegerField(primary_key=True)
    