from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'topic.html',d)

def webpage(request):
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'webpage.html',d)

def AccessRecords(request):
    QLAO=AccessRecords.objects.all()
    d={'QLAO':QLAO}
    return render(request,'accessrecords.html',d)

def insert_topic(request):
    tn=input('enter topic')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    return HttpResponse('Topic inserted')
def insert_webpage(request):
    tn=input('enter topic')
    n=input('enter name')
    u=input('enter url')
    TO=Topic.objects.get(topic_name=tn)
    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NWO.save()
    return HttpResponse('webpage inserted')

def insert_accessrecords(request):
    pk=int(input('enter topic'))
    a=input('enter author')
    d=input('enter date')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecords.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    return HttpResponse('AccessRecords inserted')
