from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
def captain(request):
    return HttpResponse('Virat Kohli is the best batsman')