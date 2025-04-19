from django.shortcuts import render

# Create your views here.
def Builtinfilters(request):
    d = {'data': 'This is a builtin filter example'}
    return render(request, 'Builtinfilters.html',d)