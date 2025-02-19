from django.shortcuts import render

# Create your views here.
def Food(request):
    return render(request,'Food.html')