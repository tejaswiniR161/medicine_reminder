from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import tablet
# Create your views here.

@login_required(login_url='/login')
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'home.html')

def logIn(r):
    if r.method=="POST":
        e=r.POST.get("e")
        pwd=r.POST.get("pwd")
        u=authenticate(username=e,password=pwd)
        if u is not None:
            auth_login(r,u)
            r.session['e']=e
            print("logged in")
            return JsonResponse({"l":"valid"})
        else:
            print("failed login")
            return JsonResponse({"l":"invalid"})
            
    return render(r,'login.html')

def signup(r):
    return render(r,'signup.html')

def SignUpSave(r):
    fn=r.POST.get("fn")
    sn=r.POST.get("sn")
    e=r.POST.get("e")
    pwd=r.POST.get("pwd")
    u=r.POST.get("e")
    #create_user(username, email=None, password=None, **extra_fields)
    t=User.objects.create_user(u,e,pwd)
    t.first_name=fn
    t.last_name=sn
    t.save()
    tab=tablet.objects.create(uid=t)
    return HttpResponseRedirect("/login")

def logout(r):
    del r.session['e']
    auth_logout(r)
    return HttpResponseRedirect("/login")
    #return render(r,'login.html')