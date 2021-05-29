from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from . import Fileoper
import markdown

# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("Encyclopedia:wiki", args=["MAINPAGE"]))
    
def content(request):
    return render(request, "Encyclopedia/content.html", {
        "Files": Fileoper.totalFiles()
    })

def create(request):    
    return HttpResponse("Create Page")

def random(request):    
    return HttpResponse("Random Page")

def search(request):    
    req = request.GET["q"]
    return HttpResponseRedirect(reverse("Encyclopedia:wiki", args = [req.upper()]))

def wiki(request, reqPage):
    filename = ''
    for ch in reqPage:
        if ch == ' ':
            continue
        filename += ch.capitalize()
    f = Fileoper.getFile(filename) 

    if f:
        html = markdown.markdown(f)
        return render(request, "Encyclopedia/index.html", {
            "title": filename,
            "content": html
        })

    else:
        return render(request, "Encyclopedia/fail.html", {
            "title": reqPage
        })