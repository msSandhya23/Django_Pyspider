from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def djForm(request):
    ESFO = StudentForm()
    if request.method == 'POST':
        return HttpResponse()
    d = {'ESFO':ESFO}
    return render(request,'djForm.html',d)