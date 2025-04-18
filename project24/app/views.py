from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def djForm(request):
    ESFO = StudentForm()
    d = {'ESFO':ESFO}
    if request.method == 'POST':
        SFOWD = StudentForm(request.POST)
        if SFOWD.is_valid():
            return HttpResponse(str(SFOWD.cleaned_data))
    return render(request,'djForm.html',d)