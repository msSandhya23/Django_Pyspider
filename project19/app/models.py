from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=14)
    loc = models.CharField(max_length=13)
    
class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10)
    job = models.CharField(max_length=9)
    mgr = models.IntegerField()
    hiredate = models.DateField()
    sal = models.FloatField()
    comm = models.FloatField()
    deptno = models.ForeignKey(Dept, on_delete=models.CASCADE)
