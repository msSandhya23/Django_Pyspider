from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.
def Student_insert(request):
    ESTMFO = StudentModelForm()
    d = {'ESTMFO':ESTMFO}
    
    if request.method == 'POST':
        STMFDO = StudentModelForm(request.POST)
        if STMFDO.is_valid():
            STMFDO.save()
            return HttpResponse('Data Inserted')
        else:
            return HttpResponse('Data Not Inserted')
    return render(request, 'Student_insert.html',d)