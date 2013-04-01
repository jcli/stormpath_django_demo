from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django import forms
from bookmark.bookmark_user import User
from bookmark.stormpath_admin import Admin

def index(request):
    # check if the user is logged in
    username=request.session.get('user', False);
    if username:
        print ("logged in as ", username)

        # if logged in display bookmark view
#        return HttpResponse("logged in as " + username.username)
        return render_to_response('bookmark/user_bookmark.djhtml')
    else:
        # redirect to the login view
        return HttpResponseRedirect('/bookmark/signin/')
  
def user_signin(request):
    if (request.method=='POST'):
        # perform signin
        user_email = request.POST['user_email']
        password = request.POST['password']
        user = Admin.user_signin(user_email, password, 'bookmark_django')
        if (not user):
            return HttpResponseRedirect('/bookmark/signin/')
        else:
            # write session variable
            request.session['user'] = user
            return HttpResponseRedirect('/bookmark/')
    else:
        # display signin
        context = Context({
            'signin':'Bookmark Manager'
        })
        return render_to_response('bookmark/signin.djhtml', context, context_instance=RequestContext(request))           
def user_signup(request):
    if (request.method=='POST'):
        user_email = request.POST['user_email']
        password = request.POST['password']
        password2 = request.POST['password_again']

        if (password!=password2):
            return HttpResponseRedirect('/bookmark/signup/')
        user = Admin.user_signup(user_email, password, 'bookmark_django')
        if (user==None):
            return HttpResponseRedirect('/bookmark/signup/')

        # changed session to loggedin
        request.session.set('user', user)
            
        return HttpResponseRedirect('/bookmark/')
    else:
        context = Context({
            'signup':'Bookmark Manager'
        })
        return render_to_response('bookmark/signup.djhtml', context, context_instance=RequestContext(request))

def user_signout(request):
    #delete the session variable
    request.session.flush()
    return HttpResponseRedirect('/bookmark/')
    
def user_view(request):
    user_email = request.POST['user_email']
    password = request.POST['password']

    print (user_email)
    print (password)

    return HttpResponse("thank you")
