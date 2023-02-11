from django.contrib import admin
from django.urls import path
from Jobpost import views

urlpatterns = [
    path("",views.index,name="index"),
    path("addpost",views.addpost,name="addpost"),
    path("login",views.loginpage,name="loginpage"),
    path("logout",views.logoutuser,name="logout"),
    path("jobpost",views.viewuser,name="jobpost"),
    path("notification",views.notification,name="notification")
]