from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def display_topics(request):
    QTTO = Topic.objects.all()
    d = {'QTTO':QTTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QLWO = Webpage.objects.all()
    d1 = {'QLWO':QLWO}
    return render(request,'display_webpages.html',d1)

def display_AccessRecord(request):
    QLAR = AccessRecord.objects.all()
    d2 = {'QLAR':QLAR}
    return render(request,'display_AccessRecord.html',d2)
def insert_topic(request):
    tn = input('enter the topic name')
    TTO = Topic.objects.get_or_create(topic_name=tn)
    if TTO[1]:
        return HttpResponse(f'{tn} is inserted')
    else:
        return HttpResponse(f'{tn} is Already exit')
    
def insert_webpage(request):
    tn = input('enter the topic name')
    LTO = Topic.objects.get_or_create(topic_name=tn)
    if LTO:
        na = input('enter name')
        ur = input('enter url')
        em = input('enter email')
        TO = LTO[0]
        TWO = Webpage.objects.get_or_create(topic_name = TO,name = na,url = ur,email = em)
        if TWO[1]:
            return HttpResponse(f'{na} is created')
        else:
            return HttpResponse(f'{na} is not created')

def insert_AccessRecord(request):
    pk = input('Enter pk of webpage')
    WO = Webpage.objects.get(pk=pk)
    date = input('Enter date ')
    author = input('Enter author')
    TAO = AccessRecord.objects.get_or_create(name = WO,date=date,author=author)
    if TAO[1]:
        return HttpResponse(f'{pk} is created')
    else:
        return HttpResponse(f'{pk} is not created')
    