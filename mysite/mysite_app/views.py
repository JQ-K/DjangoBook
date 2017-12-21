from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context
import datetime

def hello(request):
    return HttpResponse("Helo world")

def current_datetime(request):
    current_datetime = datetime.datetime.now()
    return render_to_response('current_datetime.html',locals())

    
def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = loader.get_template('hours_head.html')
    html= t.render({'hour_offset':offset,'next_time':dt})
    # html = "<html><body> in {} hour(s), it will be {}.</body></html>".format(offset, dt)
    return HttpResponse(html)
