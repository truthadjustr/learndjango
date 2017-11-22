from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request,"main.html",{})

def hello(request):
    return HttpResponse("<h2>hello</h2>")
