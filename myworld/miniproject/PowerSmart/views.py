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
        try:
            data = USERS.objects.get(MailID=umail)
            if data.Password == upw:
                request.session['id'] = data.id
                return redirect('/PowerSmart/home/')
            else:
                messages.error(request, 'Wrong password!')
        except USERS.DoesNotExist:
            messages.error(request, 'Account does not exist. Check mail id')
        
        return redirect('/PowerSmart/home/')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method == 'POST':
        email = request.POST.get('mail')
        password = request.POST.get('password')

        if USERS.objects.filter(MailID=email).exists():
            return render(request, 'signup.html', {'display_alert': True, 'error': 'THE ACCOUNT ALREADY EXISTS! TRYING LOGGING IN'})

        user = USERS.objects.create(
            FirstName=request.POST['fname'],
            LastName=request.POST['lname'],
            MailID=request.POST['mail'],
            Password=request.POST['password']
        )
        #request.session['id'] = user.id
        request.session.save()

        return redirect('login') 
    
def home(request) :
   i = request.session['id']
   udet = USERS.objects.get(id = i)
   context = {
      'fname' : udet.FirstName,
      'lname' : udet.LastName
   }
   return render(request, 'home.html', context)