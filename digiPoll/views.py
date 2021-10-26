from typing import ContextManager
from django.shortcuts import render,HttpResponse
from django.template import loader

def home(request):
    context={}
    return render(request,'home.html',context)


def create(request):
    context={}
    return render(request,'create.html',context)

def vote(request):
    context={}
    return render(request,'vote.html',context)

def results(request):
    context={}
    return render(request,'results.html',context)

#def home(request):  
#    template = loader.get_template('home.html') # getting our template  
#    return HttpResponse(template.render()) 