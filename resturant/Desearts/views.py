from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Steam(request):
    return HttpResponse('Steam')
def HalfSteam(request):
    return render(request,'Chenapoda.html')
