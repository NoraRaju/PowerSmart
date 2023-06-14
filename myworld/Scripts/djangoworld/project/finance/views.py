from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import USERS

# Create your views here.

def login(request) : 
      message = ""
      wrongpw_alert = False
      if request.method == 'GET' :
        return render(request, 'login.html')
      elif request.method=='POST' :
        umail = request.POST.get('email')
        upw = request.POST.get('logpw')
        if USERS.objects.filter(MailID=umail,Password=upw) :
            data = USERS.objects.get(MailID=umail,Password=upw)
            request.session['id']=data.id
            return redirect('/finance/home/')
        else :
            message = 'WRONG PASSWORD! Try Again'
            wrongpw_alert = True
            context = {
              'error' : message,
              'display_alert': wrongpw_alert
            }
            return render(request, 'login.html', context)
              
      

def signup(request) :
    message = ""
    display_alert = False
    if request.method=='GET' : 
      return render(request, 'signup.html')
    elif request.method=='POST' :
      x = USERS.objects.filter(MailID=request.POST['mail']).values()
      if len(x) :
          message = 'THE ACCOUNT ALREADY EXISTS! TRYING LOGGING IN'
          display_alert = True
      if display_alert is not True :
          USERS.objects.create(FirstName = request.POST['fname'], 
                               LastName = request.POST['lname'], 
                               MailID = request.POST['mail'], 
                               Password = request.POST['password'])
      context = {
              'error' : message,
              'display_alert': display_alert
          }
      return render(request, 'login.html', context)
    
def home(request) :
   i = request.session['id']
   udet = USERS.objects.get(id = i)
   context = {
      'fname' : udet.FirstName,
      'lname' : udet.LastName
   }
   return render(request, 'home.html', context)