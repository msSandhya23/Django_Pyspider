from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def HydrabadiDumBiriyani(request):
    return HttpResponse('one of my fav food')
def dumBiriyani(request):
    return render(request,'ChickenBiriyani.html')