from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from . import Fileoper
import markdown
from .models import filenameloc, TotalFiles

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST["title"]
        article = request.POST["article"]
        finalTitle = ''
        for ch in title:
            if ch == ' ':
                continue
            finalTitle += ch.capitalize()
        if filenameloc.objects.get(tisearch=finalTitle):
            messages.error(request, "Article title already present")

        else:
            var = filenameloc(title=title, tisearch=finalTitle)
            var.save()
            #increment number
            default_storage.save(f"Files/{finalTitle}.md", ContentFile(article))  
            messages.success(request, "Article is saved")
                 
        return render(request, "Encyclopedia/create.html")

    return HttpResponseRedirect(reverse("Encyclopedia:wiki", args=["MAINPAGE"]))
    
def content(request):
    return render(request, "Encyclopedia/content.html", {
        "files": filenameloc.objects.all()
    })

def create(request):    
    return render(request, "Encyclopedia/create.html")

def random(request):    
    filename = Fileoper.randomFile()
    return HttpResponseRedirect(reverse("Encyclopedia:wiki", args=[filename]))

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

def edit(request, reqPage):
    if request.method == 'POST':
        title = request.POST["title"]
        article = request.POST["article"]
        Fileoper.saveFile(title, article)
        messages.success(request, "File updated successfully...")

    f = Fileoper.getFile(reqPage) 
    if f:
        return render(request, "Encyclopedia/edit.html", {
            "title": reqPage,
            "content": f
        })

    else:
        return render(request, "Encyclopedia/fail.html", {
            "title": reqPage
        })