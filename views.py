# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from ywy.wan.models import author,book


def search_form(request):
    return render_to_response('search_form.html')



def search(request):
    if 'q' in request.GET and request.GET['q']:
        q=request.GET['q']
        author_id=author.objects.filter(name=q)
        books=book.objects.filter(authorid=author_id)
        return render_to_response('search.html',  {'books': books})
    else:   
        return render_to_response('search_form.html', {'error': True})


def service(request):
    if 'p' in request.GET and request.GET['p']:
        p= request.GET['p']       
        books=book.objects.get(title=p)
        authors=author.objects.get(authorid=books.authorid.authorid)
        return render_to_response('service.html', locals())


def delete(request):
        select= request.GET['select']
        book.objects.get(title=select).delete()
        return render_to_response('delete.html') 



