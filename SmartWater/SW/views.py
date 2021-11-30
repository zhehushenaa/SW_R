from django.shortcuts import render
from django.http import HttpResponse





def index(request):
    context={}
    context["hello"]='hello'
    return render(request,'indextest1.html',context)


def back(request):
    context={}
    context["hello"]='hello'
    return render(request,'back.html',context)

def sensorscan(request):
    context={}
    context["hello"]='hello'
    return render(request,'sensorscan.html')

def sensorrecord(request):
    context={}
    context["hello"]='hello'
    return render(request,'sensorrecord.html')


def scandata1(request):
    context={}
    context["hello"]='hello'
    return render(request,'scandata1.html')