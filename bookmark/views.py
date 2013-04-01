from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django import forms
from stormpath.client import ClientBuilder

def index(request):
    httplib2.Http(disable_ssl_certificate_validation=True).request('https://www./')
    # create stormpath client
    api_key_file = 'bookmark/stormpath_api_key/apiKey.yml'
    client = ClientBuilder().set_api_key_file_location(api_key_file).build()

    tenant = client.current_tenant

#    applications = tenant.applications
    
    # for app in applications:
    #     print('Application ' + app.name)
        
    context = Context({
        'signin':'Bookmark Manager'
    })
    return render_to_response('bookmark/signin.djhtml', context, context_instance=RequestContext(request))

def user_signup(request):
    context = Context({
        'signup':'Bookmark Manager'
    })
    return render_to_response('bookmark/signup.djhtml', context, context_instance=RequestContext(request))
    
def user_view(request):
    user_email = request.POST['user_email']
    password = request.POST['password']

    print (user_email)
    print (password)

    return HttpResponse("thank you")

def user_signup_response(request):

    return HttpResponse("thank you for signing up")