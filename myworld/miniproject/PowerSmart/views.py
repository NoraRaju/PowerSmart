from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import USERS

def login(request) :
    if request.method=='GET' :
        return render(request, 'login.html')
    elif request.method=='POST' :
        
        return redirect('/PowerSmart/home')

def signup(request) :
    if request.method=='GET' :
        return render(request, 'signup.html')
    elif request.method=='POST' :
        
        return redirect('/PowerSmart/login')
    
def home(request) :
    return render(request, 'home.html')