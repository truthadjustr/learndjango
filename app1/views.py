from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.
def main(request):
    #today = datetime.datetime.now().date()
    today = str(datetime.datetime.now())
    return render(request,"main.html",{"today":today})

def hello(request,param):
    return HttpResponse("<h2>hello %s</h2>" % ("stranger" if not param else param))

def yyyymmdd(request,yyyy,mm,dd):
    # url params are received as string
    x = "%s/%s/%s" % (yyyy,mm,dd)
    return HttpResponse("<h3>Schedule: %s</h3>" % x)
