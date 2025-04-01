from django.shortcuts import render

# Create your views here.
def htmlfile(request):
    return render(request,'htmlfile.html')