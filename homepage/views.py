from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'homepage/bodymain.html')
def login(request,pk):
    return render(request,'homepage/index.html',{'type':pk})