from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q
from django.db.models import Prefetch
# Create your views here.
def display_topics(request):
    QTTO = Topic.objects.all()
    d = {'QTTO':QTTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    QLWO = Webpage.objects.all()
    #QLWO =Webpage.objects.filter(topic_name="Vollyball")
    QLWO = Webpage.objects.filter(topic_name__topic_name="Vollyball")
    QLWO = Webpage.objects.exclude(topic_name__topic_name="Vollyball")
    QLWO = Webpage.objects.all()[0:3:1]
    QLWO = Webpage.objects.all()[::-1]
    QLWO = Webpage.objects.all().order_by('name')
    QLWO = Webpage.objects.all().order_by('-name')
    QLWO = Webpage.objects.all()
    QLWO = Webpage.objects.filter(url__endswith='com')
    QLWO = Webpage.objects.filter(url__startswith='https')
    QLWO = Webpage.objects.filter(name__contains='m')
    QLWO = Webpage.objects.filter(url__in=['https://www.google.com','https://www.facebook.com'])
    QLWO = Webpage.objects.all()
    QLWO = Webpage.objects.filter(name__regex='MSD')
    QLWO = Webpage.objects.all()
    QLWO = Webpage.objects.filter(pk__gt=2)
    QLWO = Webpage.objects.filter(pk__lt=3)
    QLWO = Webpage.objects.filter(pk__gte=4)
    QLWO = Webpage.objects.filter(pk__lte=3)
    QLWO = Webpage.objects.all()
    QLWO = Webpage.objects.filter(Q(name__startswith='m')|Q(name__startswith='s'))
    QLWO = Webpage.objects.filter(Q(name__startswith='m')|Q(name__endswith='s'))
    d1 = {'QLWO':QLWO}
    return render(request,'display_webpages.html',d1)

def display_AccessRecord(request):
    QLAR = AccessRecord.objects.all()
    QLAR = AccessRecord.objects.filter(date__year=2022)
    QLAR = AccessRecord.objects.filter(date__day = 19)
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
    
def TopicToWebpageByPR(request):
    QLTWO = Webpage.objects.prefetch_related('topic_name').all()
    return render(request,'TopicTowebpageByPR.html') 