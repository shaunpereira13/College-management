from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from django.contrib import messages
from .forms import *
from django.db.models import Avg



@login_required(login_url='login/')
def studentdetails(request,roll_no):
    if not StudentModel.objects.filter(roll_no=roll_no).exists():
        messages.error(request, 'roll number does not exists.')
        return redirect("home")
    data={}
    data['info']= StudentModel.objects.get(roll_no=roll_no)
    data['marks']=marksModel.objects.filter(student_id=roll_no)
    return render(request,'student/studentdetails.html', data)
    # print(roll_no)
    # data=StudentModel.objects.raw('SELECT * FROM student_StudentModel')
    # print(data)
    # for p in StudentModel.objects.raw('SELECT * FROM student_StudentModel WHERE roll_no=roll_no'):
    #     data=p
    #     print(data)


@login_required(login_url='loginteach/')
def teacherdetails(request,trno):
    if not TeacherModel.objects.filter(trno=trno).exists():
        messages.error(request, 'Teacher number does not exists.')
        return redirect("home")
    data={}
    x= TeacherModel.objects.get(trno=trno)
    data["info"]=x
    data["subjects"]=teachesub.objects.filter(teacher_id=x.id)
    
    return render(request,'student/teacherdetails.html',data)

def logouts(request):
    logout(request)
    return redirect('home')

@login_required(login_url='loginteach/')
def marks(request,subid):
    # a=marksModel.objects.filter(subject_id=subid).aggregate(a=(''))
    data={}
    data['sub']=marksModel.objects.filter(subject_id=subid)
    data["marks"]=marksModel.objects.filter(subject_id=subid)
    return render(request,'student/marks.html/',data)




def updatemarks(request,pk):
    row=marksModel.objects.get(id=pk)
    f=marksform(instance=row)
    subid=marksModel.objects.filter(id=pk)
    if request.method=='POST':
        f=marksform(request.POST,request.FILES,instance=row)
        if f.is_valid():
            f.save()
            return redirect('/marks/4/')
    return render(request,'student/marksenter.html',{'form':f})

def createstud(request):
    form=studentform()
    if request.method=='POST':
        f=studentform(request.POST, request.FILES)
        if f.is_valid():
            f.save()
            return redirect('/')
    return render(request,'student/createstud.html',{'form':form})



def deletestudent(request,subid):
    pr=StudentModel.objects.get(id=subid)
    if request.method=='POST':
        pr.delete()  
    return 
