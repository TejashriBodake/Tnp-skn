from django.shortcuts import render,HttpResponse
from .models import Jobpost,Notification
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect

def index(request):
    post_list=Jobpost.objects.all()
    noti_list=Notification.objects.all()
    return render(request,"index.html",{'post_list':post_list,'noti_list':noti_list})

def addpost(request):
    if request.method == "POST":
        jobName=request.POST.get('jobName')
        jobDescription=request.POST.get('jobDescription')
        addpost=Jobpost(jobName=jobName,jobDescription=jobDescription)
        addpost.save()
        messages.success(request, 'Register sucessfully!!.')
    return render(request,"addpost.html")


def loginpage(request):
    if request.method == "POST":
        username=request.POST.get('name')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/addpost")
        else:
            messages.success(request, 'Login unsuccessfull!!.')
    
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")


def viewuser(request):
    user_list=Jobpost.objects.all()
    return render(request,"jobpost.html",{'user_list':user_list})


def notification(request):
    if request.method == "POST":
        Addnotification=request.POST.get('Addnotification')
        notification=Notification(Addnotification=Addnotification)
        notification.save()
        messages.success(request, 'Notification Added sucessfully!!.')
    return render(request,"notification.html")
        

