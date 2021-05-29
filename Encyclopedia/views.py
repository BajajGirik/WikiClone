from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . import Fileoper

# Create your views here.
def index(request):
    return HttpResponseRedirect(f"wiki/MAINPAGE")
    
def content(request):
    return HttpResponse("Content Page") 

def create(request):    
    return HttpResponse("Create Page")

def random(request):    
    return HttpResponse("Random Page")

def wiki(request, reqPage): 
    filename = ''
    for ch in reqPage:
        if ch == ' ':
            continue
        filename += ch.capitalize()

    f = Fileoper.getFile(filename)
    if f:
        return render(request, "Encyclopedia/index.html")    
    else:
       return HttpResponse("Fail")     