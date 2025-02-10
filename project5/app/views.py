from django.shortcuts import render

# Create your views here.
def jinjaprint(request):
    d={"Subject":'python',"price":3200}
    return render(request,'jinjaprint.html',context=d)