from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def School_insert(request):
    ESFO = SchoolForm()
    d = {'ESFO':ESFO}
    if request.method == 'POST':
        SFDO = SchoolForm(request.POST)
        if SFDO.is_valid():
            sn = SFDO.cleaned_data['Scname']
            sl = SFDO.cleaned_data['ScLocation']
            #sp = SFDO.cleaned_data['ScPrinciple ']
            SFDO = School.objects.get_or_create(Scname = sn,ScLocation = sl)
            return HttpResponse('SchoolForm Created')
    
    return render(request,'School_insert.html',d)

def Student_insert(request):
    ESTFO = StudentForm()
    if request.method == 'POST':
        ESTFO = StudentForm(request.POST)
        if ESTFO.is_valid():
            sn = ESTFO.cleaned_data['Scname']
            st = ESTFO.cleaned_data['StName']
            sa = ESTFO.cleaned_data['StAge']
            ESTFO = Student.objects.get_or_create(ScName = sn,StName = st,StAge = sa)
            return HttpResponse('StudentForm Created')
    d = {'ESTFO':ESTFO}
    return render(request,'Student_insert.html')