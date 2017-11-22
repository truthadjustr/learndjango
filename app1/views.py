from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request,"main.html",{})

def hello(request,param):
    return HttpResponse("<h2>hello %s</h2>" % ("stranger" if not param else param))
