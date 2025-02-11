from django.shortcuts import render

# Create your views here.
def condition(request):
    d = {'a': 10,'name':'sandhya','b':20,'c':30}
    return render(request,'conditions.html',context=d)