from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader, RequestContext
from django import forms
from bookmark.bookmark_user import User
from bookmark.stormpath_admin import Admin

def index(request):
    # check if the user is logged in
    username=request.session.get('username', False);
    if username:
        print ("logged in as ", username)
    else:
        print ("not logged in")
        
    # if logged in display bookmark view

    # else display login view
    

    print (Admin.app_url('bookmark_django'))
    
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