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
            finalTitle += ch.upper()
        try:
            temp = filenameloc.objects.get(tisearch=finalTitle)
            messages.error(request, "Article title already present")

        except:
            var = filenameloc(title=title, tisearch=finalTitle)
            var.save()
            fir = TotalFiles.objects.first()
            fir.total += 1
            fir.save()
            default_storage.save(f"Files/{finalTitle}.md", ContentFile(article))  
            messages.success(request, "Article is saved")
                 
        return render(request, "Encyclopedia/create.html", {
            "TAP": TotalFiles.objects.first()
        })

    return HttpResponseRedirect(reverse("Encyclopedia:wiki", args=["MAINPAGE"]))
    
def content(request):
    return render(request, "Encyclopedia/content.html", {
        "TAP": TotalFiles.objects.first(),
        "files": filenameloc.objects.all()
    })

def create(request):    
    return render(request, "Encyclopedia/create.html",{
        "TAP": TotalFiles.objects.first()
    })

def random(request):    
    filename = Fileoper.randomFile()
    return HttpResponseRedirect(reverse("Encyclopedia:wiki", args=[filename]))

def search(request):    
    req = request.GET["q"]
    filename = ''
    for ch in req:
        if ch == ' ':
            continue
        filename += ch.upper()
    
    try:
        temp = filenameloc.objects.get(tisearch=filename)
        return HttpResponseRedirect(reverse("Encyclopedia:wiki", args = [filename]))
    except:
        return HttpResponseRedirect(reverse("Encyclopedia:wiki", args = [req]))


def wiki(request, reqPage):
    try:
        temp = filenameloc.objects.get(tisearch=reqPage)
        f = default_storage.open(f"Files/{reqPage}.md").read().decode("utf-8")
        html = markdown.markdown(f)
        return render(request, "Encyclopedia/index.html", {
            "TAP": TotalFiles.objects.first(),
            "title": reqPage,
            "content": html
        })

    except:
        return render(request, "Encyclopedia/fail.html", {
            "TAP": TotalFiles.objects.first(),
            "title": reqPage
        })

def edit(request, reqPage):
    if request.method == 'POST':
        title = request.POST["title"]
        article = request.POST["article"]
        tisearch = filenameloc.objects.get(title=title).tisearch
        
        default_storage.delete(f"Files/{tisearch}.md")
        default_storage.save(f"Files/{tisearch}.md",ContentFile(article))

        messages.success(request, "File updated successfully...")

    f = default_storage.open(f"Files/{reqPage}.md").read().decode("utf-8")
    if f:
        return render(request, "Encyclopedia/edit.html", {
            "TAP": TotalFiles.objects.first(),
            "title": filenameloc.objects.get(tisearch=reqPage),
            "content": f
        })

    else:
        return render(request, "Encyclopedia/fail.html", {
            "TAP": TotalFiles.objects.first(),
            "title": reqPage
        })