from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *

def home(request):
    try:
        if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email']
            phone=request.POST['phone']
            queries=request.POST['queries']
            Contactus.objects.create(name=name, email=email, phone=phone,queries=queries)
    except Exception as e:
        print(e)
    return render(request,'homepage/bodymain.html')

def loginstudent(request,pk):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        roll_no=request.POST['Rollno']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exists.')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(f"/studentdet/{roll_no}/")
            
        else:
            messages.error(request, 'username or password wrong.')

        print(request.POST)
    return render(request,'homepage/index.html',{'type':pk})


def loginteacher(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        trno=request.POST['Tr_no']
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, 'username does not exists.')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect(f'/teacherdet/{trno}/')
        else:
            messages.error(request, 'username or password wrong.')

        print(request.POST)
    return render(request,'homepage/index.html')
    