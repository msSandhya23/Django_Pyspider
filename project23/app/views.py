from django.shortcuts import render
from django.http import HttpResponse
from app.views import *
# Create your views here.
def School(request):
    
    return render(request,'School.html')