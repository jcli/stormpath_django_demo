from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    template = loader.get_template('bookmark/index.djhtml')
    context = Context({
            'latest_poll_list': "lkajdsf",
            })
    return HttpResponse(template.render(context))