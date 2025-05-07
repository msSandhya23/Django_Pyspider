from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.

 #FBV for returning string as Response

def fbv(request):
     return HttpResponse('Hi')
 
 
 #CBV for returning string as Response
class CBV(View):
    def get(self,request):
        return HttpResponse('Hello')
    

#FBV for returning string as HTML page
def fbv(request):
    return render(request,'fbv.html')


#FBV for returning string as HTML page
class CBV(View):
    def get(self,request):
        return render(request,'cbv.html')
    
    
#Insert Data into School By using FBV
def insert_school_by_fbv(request):
    ESFO=SchoolMF()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('DOne')
        else:
            return HttpResponse('Invalid')
    return render(request,'insert_student_fbv.html',d)


    
   