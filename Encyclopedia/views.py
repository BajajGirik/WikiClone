from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . import Fileoper

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("Encyclopedia:wiki", args=["MAINPAGE"]))
    
def content(request):
    return HttpResponse("Content Page") 

def create(request):    
    return HttpResponse("Create Page")

def random(request):    
    return HttpResponse("Random Page")

def search(request):    
    req = request.GET["q"]
    return HttpResponseRedirect(reverse("Encyclopedia:wiki", args = [req]))

def wiki(request, reqPage):
    filename = ''
    for ch in reqPage:
        if ch == ' ':
            continue
        filename += ch.capitalize()
    f = Fileoper.getFile(filename) 

    if f:
        return render(request, "Encyclopedia/index.html", {
        "content": f
    })

    else:
        return HttpResponse("Fail")