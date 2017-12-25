# coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context
from django.core.mail import send_mail
import datetime
from mysite_app.models import Book

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


def display_meta(request):
    values = request.META.items()
    #values.sort()
    t = loader.get_template('display_meta.html')
    html = t.render({'values':values})
    return HttpResponse(html)

def search_form(request):
    return render_to_response('search_from.html')

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books':books,'query':q})
    return render_to_response('search_from.html',{'errors':errors})


def contact(request):
    errors=[]
    if request.method =="POST":
        if not request.POST.get('subject',''):
            errors.append('Enter a subject')
        if not request.POST.get('message',''):
            errors.append('Enter a message')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            send_mail(
                    request.POST['subject'],
                    request.POST['message'],
                    request.POST.get('email','1099949903@qq.com'),
                    ['1099949903@qq.com'],
                    fail_silently=True,
                    )
    return render_to_response('contact_form.html',
            {'errors':errors})
