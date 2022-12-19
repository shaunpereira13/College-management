from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from django.contrib import messages

data = {}


@login_required(login_url='login/')
def studentdetails(request,roll_no):
    if not StudentModel.objects.filter(roll_no=roll_no).exists():
        messages.error(request, 'roll number does not exists.')
        return redirect("/home")
    data["student_info"] = StudentModel.objects.get(roll_no=roll_no)
    return render(request,'student/studentdetails.html', context=data)


@login_required(login_url='loginteach/')
def teacherdetailss(request):
    return render(request,'student/teacherdetails.html')

def logouts(request):
    logout(request)
    return redirect('home')

def marks(request):
    return render(request,'student/marks.html')
