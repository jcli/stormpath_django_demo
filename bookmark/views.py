from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    context = Context({
        'signin':'Bookmark Manager'
    })
    return render_to_response('bookmark/signin.djhtml', context)