from django.http import HttpResponse
from django.template import loader, Context
import datetime

def hello(request):
    return HttpResponse("Helo world")

def current_datetime(request):
    now = datetime.datetime.now()
    t = loader.get_template('current_datetime.html')
    html = t.render({'current_datetime':now})
    return HttpResponse(html)

    
def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body> in {} hour(s), it will be {}.</body></html>".format(offset, dt)
    return HttpResponse(html)
