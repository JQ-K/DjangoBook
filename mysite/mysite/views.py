from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Helo world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body> It is now {}.</body></html>".format(now) 
    return HttpResponse(html)
