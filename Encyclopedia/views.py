from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        return HttpResponseRedirect(f"/{request.POST.get('q')}")
    return render(request, "Encyclopedia/index.html")