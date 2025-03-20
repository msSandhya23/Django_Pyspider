from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_emp(request):
    eno = int(input('Enter employee number: '))
    ename = input('Enter employee name: ')
    job = input('Enter employee job: ')
    sal = float(input('Enter employee salary: '))
    comm = input('Enter employee commission: ')
    if comm:
        comm = float(comm)
    else:
        comm = None
    hiredate = input('Enter employee hiredate: ')
    deptno = int(input('Enter employee department number: '))
    DO = Dept.objects.get(deptno=deptno)
    mgr = input('Enter employee manager NO: ')
    if mgr:
        MO = Emp.objects.get(empno = int(mgr))
    else:
        MO = None
    TEO = Emp.objects.get_or_create(empno = eno, ename = ename, job = job, mgr = MO, hiredate = hiredate, sal = sal, comm = comm, deptno = DO)
    if TEO[1]:
        return HttpResponse('Employee added successfully')
    else:
        return HttpResponse('Employee already exists')

def empToDeptJoin(request):
    QLEDO = Emp.objects.all().select_related('deptno')
    d = {'QLEDO':QLEDO}
    return render(request,'empToDeptJoin.html',d)  
    