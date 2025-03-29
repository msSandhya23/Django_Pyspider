from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models import Prefetch
from django.db.models import Min,Max,Avg,Count,Sum
from django.db.models.functions import Length
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
    QLEDO = Emp.objects.select_related('deptno').filter(ename__startswith = 'S')
    QLEDO = Emp.objects.select_related('deptno').filter(ename__endswith = 'T')
    QLEDO = Emp.objects.select_related('deptno').filter(ename__contains = 'a')
    QLEDO = Emp.objects.select_related('deptno').filter(job = 'SALESMAN')
    QLEDO = Emp.objects.select_related('deptno').filter(sal__gt = 1000)
    QLEDO = Emp.objects.select_related('deptno').filter(comm__isnull = True)
    QLEDO = Emp.objects.select_related('deptno').filter(hiredate__year = 1981)
    QLEDO = Emp.objects.select_related('deptno').filter(hiredate__year = 1999, hiredate__month = 12)
    QLEDO = Emp.objects.select_related('deptno').filter(mgr__isnull = True)
    QLEDO = Emp.objects.select_related('deptno').filter(mgr__isnull = False)
    QLEDO = Emp.objects.select_related('deptno').filter(deptno = 10)
    QLEDO = Emp.objects.select_related('deptno').filter(deptno__dname = 'RESEARCH')
    QLEDO = Emp.objects.select_related('deptno').filter(deptno__loc = 'DALLAS')
    QLEDO = Emp.objects.select_related('deptno').filter(deptno__deptno = 20)
    
    avgsal = Emp.objects.aggregate(agsal = Avg('sal'))['agsal']
    print(avgsal)
    QLEDO = Emp.objects.select_related('deptno').filter(sal__gt = avgsal)
    QLEDO = Emp.objects.annotate(loe = Length('ename')).filter(loe = 5)
    
    d = {'QLEDO':QLEDO}
    return render(request,'empToDeptJoin.html',d)  

def EmpToMgr(request):
    QLEMO = Emp.objects.all().select_related('mgr')
    QLEMO = Emp.objects.select_related('mgr').filter(ename__startswith = 'S')
    QLEMO = Emp.objects.select_related('mgr').filter(ename__endswith = 'T')
    QLEMO = Emp.objects.select_related('mgr').filter(ename__contains = 'a')
    QLEMO = Emp.objects.select_related('mgr').filter(job = 'SALESMAN')
    QLEMO = Emp.objects.select_related('mgr').filter(sal__gt = 1000)
    QLEMO = Emp.objects.select_related('mgr').filter(comm__isnull = True)
    QLEMO = Emp.objects.select_related('mgr').filter(hiredate__year = 1981)
    QLEMO = Emp.objects.select_related('mgr').filter(hiredate__year = 1999, hiredate__month = 12)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__isnull = True)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__isnull = False)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__empno = 7839) 
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__ename = 'KING')
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__job = 'MANAGER')
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__hiredate__year = 1981)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__hiredate__year = 1999, mgr__hiredate__month = 12)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__sal__gt = 1000)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__comm__isnull = True)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__isnull = True)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__isnull = False)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__empno = 7839)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__ename = 'KING')
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__job = 'MANAGER')
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__hiredate__year = 1981)    
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__hiredate__year = 1999, mgr__mgr__hiredate__month = 12)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__sal__gt = 1000)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__comm__isnull = True)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__mgr__isnull = True)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__mgr__isnull = False)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__mgr__empno = 7839)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__mgr__ename = 'KING')
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__mgr__job = 'MANAGER')
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__mgr__hiredate__year = 1981)    
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__mgr__hiredate__year = 1999, mgr__mgr__mgr__hiredate__month = 12)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__mgr__sal__gt = 1000)
    QLEMO = Emp.objects.select_related('mgr').filter(mgr__mgr__mgr__comm__isnull = True)
    d = {'QLEMO':QLEMO}
    return render(request,'EmpToMgr.html',d)
    
    
def EmpToDeptAndMgr(request):
    QLEDMO = Emp.objects.all().select_related('deptno','mgr')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(ename__startswith = 'S')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(ename__endswith = 'T')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(ename__contains = 'a')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(job = 'SALESMAN')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(sal__gt = 1000)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(comm__isnull = True)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(hiredate__year = 1981)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(hiredate__year = 1999, hiredate__month = 12)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__isnull = True)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__isnull = False)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(deptno = 10)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(deptno__dname = 'RESEARCH')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(deptno__loc = 'DALLAS')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__empno = 7839)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__ename = 'KING')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__job = 'MANAGER')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__hiredate__year = 1981)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__hiredate__year = 1999, mgr__hiredate__month = 12)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gt = 1000)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__comm__isnull = True)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__isnull = True)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__isnull = False)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__empno = 7839)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__ename = 'KING')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__job = 'MANAGER')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__hiredate__year = 1981)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__hiredate__year = 1999, mgr__mgr__hiredate__month = 12)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__sal__gt = 1000)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__comm__isnull = True)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__mgr__isnull = True)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__mgr__isnull = False)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__mgr__empno = 7839)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__mgr__ename = 'KING')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__mgr__job = 'MANAGER')
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__mgr__hiredate__year = 1981)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__mgr__hiredate__year = 1999, mgr__mgr__mgr__hiredate__month = 12)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__mgr__sal__gt = 1000)
    QLEDMO = Emp.objects.select_related('deptno','mgr').filter(mgr__mgr__mgr__comm__isnull = True)
    
    d = {'QLEDMO':QLEDMO}
    return render(request,'EmpToDeptAndMgr.html',d)

def EmpToDeptByPR(request):
    QLDO = Dept.objects.all().prefetch_related('emp_set')
    QLDO = Dept.objects.prefetch_related('emp_set').filter(dname__startswith = 'S')
    QLDO = Dept.objects.prefetch_related(Prefetch('emp_set', queryset=Emp.objects.filter(job = 'SALESMAN')))
    
    d = {'QLDO':QLDO}
    return render(request,'EmpToDeptByPR.html',d)

