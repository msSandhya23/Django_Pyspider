from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.core.mail import send_mail
# Create your views here.

def registration(request):
    EUMFO = UserForm()
    EPMFO = ProfileForm()
    d = {"EUMFO":EUMFO,"EPMFO":EPMFO}
    if request.method == 'POST' and request.FILES :
        NMUFDO = UserForm(request.POST)
        NMPFDO = ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO = NMUFDO.save(commit = False)
            pw = NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO = NMPFDO.save(commit = False)
            MPFDO.username = MUFDO
            MPFDO.save()
            send_mail('registration','Thanks for registration','sandhyabehera33090@gmail.com',[MUFDO.email],fail_silently=False)
            return HttpResponse("Registration successful!")
    
    return render(request, 'registration.html',d)