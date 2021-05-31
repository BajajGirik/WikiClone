from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from . import Fileoper
import markdown

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST["title"]
        article = request.POST["article"]
        msg = Fileoper.createFile(title,article)
        print(msg)
        if msg:
            messages.success(request, "Article is saved")
        else:
            messages.error(request, "Article title already present")
              
        
        return render(request, "Encyclopedia/create.html")

    return HttpResponseRedirect(reverse("Encyclopedia:wiki", args=["MAINPAGE"]))
    
def content(request):
    print(Fileoper.totalFiles())
    return render(request, "Encyclopedia/content.html", {
        "files": Fileoper.totalFiles()
    })

def create(request):    
    return render(request, "Encyclopedia/create.html")

def random(request):    
    return HttpResponse("Random Page")

def search(request):    
    req = request.GET["q"]
    requp = req.upper()
    filename = ''
    for ch in requp:
        if ch == ' ':
            continue
        filename += ch
    
    if Fileoper.getFile(filename):
        return HttpResponseRedirect(reverse("Encyclopedia:wiki", args = [filename]))
    else:
        return HttpResponseRedirect(reverse("Encyclopedia:wiki", args = [req]))


def wiki(request, reqPage):
    f = Fileoper.getFile(reqPage) 
    if f:
        html = markdown.markdown(f)
        return render(request, "Encyclopedia/index.html", {
            "title": reqPage,
            "content": html
        })

    else:
        return render(request, "Encyclopedia/fail.html", {
            "title": reqPage
        })