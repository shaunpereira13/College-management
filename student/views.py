from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from homepage import views 


@login_required(login_url='login/')
def studentdetails(request,roll_no):
    return render(request,'student/studentdetails.html')


@login_required(login_url='loginteach/')
def teacherdetailss(request):
    return render(request,'student/teacherdetails.html')

def logouts(request):
    logout(request)
    return redirect('home')

def marks(request):
    return render(request,'student/marks.html')
