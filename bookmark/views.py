from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from django import forms
from bookmark.stormpath_admin import Admin, UserInfo
from bookmark.models import User, Link

def index(request):
    # check if the user is logged in
    username=request.session.get('user', False);
    if username:
        # if logged in display bookmark view
        # find the user from database
        try:
            user = User.objects.filter(username=username)[0]
        except:
            user = User.objects.create(username=username)
            user.save()
            
        context = Context({
            'bookmark':'Bookmark Manager',
            'user':user,
        })        
        return render_to_response('bookmark/user_bookmark.djhtml', context, context_instance=RequestContext(request))
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
        print ("about to set session")
        request.session['user']=user
        print ("set session")
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

def user_save(request):
    if (request.method=='POST' and request.session.get('user', False)):        
        # get user from database
        user = request.session.get('user', False)
        try:
            user = User.objects.filter(username=user.username)[0]
            print ("user found in database")            
        except:
            print ("user not found in database")
            user = User.objects.create(username=user.username)
            user.save()
            print (user.username)

        link=request.POST['new_link']
        if (len(link)>1):
            user.link_set.create(linkPath=link)
    
    return HttpResponseRedirect('/bookmark/')
            