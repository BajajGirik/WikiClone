from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponseRedirect(f"wiki/{request.POST.get('q')}")
    return render(request, "Encyclopedia/index.html")

def content(request):
    return HttpResponse("Content Page") 

def create(request):    
    return HttpResponse("Create Page")

def random(request):    
    return HttpResponse("Random Page")

def wiki(request, reqPage):    
    return HttpResponse("Wiki Page")