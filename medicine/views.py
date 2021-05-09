from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import tablet
import os
# Create your views here.

@login_required(login_url='/login')
def index(r):
    em=r.session['e']
    #return HttpResponse("Hello, world. You're at the polls index.")
    u=User.objects.get(username=em)
    tab=tablet.objects.get(uid=u)
    return render(r,'home.html',{"tablets":tab.tablet_time})

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

def savetab(r):
    em=r.session['e']
    print(em)
    u=User.objects.get(username=em)
    time=r.POST.get("time")
    attr="tablet_time"
    tabobj=tablet.objects.get(uid=u)
    setattr(tabobj,attr,time)
    tabobj.save()
    fo=open("schedule.txt","w")
    fo.write(time)
    fo.close()
    os.system("mosquitto_pub -t medbox/schedule -m on")
    #msg={"topic":"medbox/runscheduler","payload":"save"}
    #msgs = [{'topic': "paho/test/multiple", 'payload': "multiple 1"}, ("paho/test/multiple", "multiple 2", 0, False)]
    #publish.single("paho/test/single", "payload", hostname="mqtt.eclipse.org")
    return JsonResponse({'d':'success'})

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