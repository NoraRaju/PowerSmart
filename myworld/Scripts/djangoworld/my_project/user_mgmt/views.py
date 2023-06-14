from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Login

# Create your views here.

def insertdata(request) :
    if request.method=='GET' :
        return render(request, 'formInsert.html')
    elif request.method=='POST' :
        Login.objects.create(UserName = request.POST['username'], 
                             MailID = request.POST['mail'], 
                             Age = request.POST['age'], 
                             DOB = request.POST['dob'], 
                             PhnNo = request.POST['phn'], 
                             Password = request.POST['pw'])
        return render(request, 'tabledisp.html')
        return HttpResponse("The values are entered into the database")
    
def displayTable(request):
    y=Login.objects.all()
    return render(request, 'tabledisp.html', {'head': y})

def editTable(request, id):
    abc = Login.objects.get(id=id)
    if request.method == 'POST' :
        abc.UserName = request.POST.get('username')
        abc.MailID = request.POST.get('mail')
        abc.Age = request.POST.get('age')
        if request.POST.get('dob') != "":
            abc.DOB = request.POST.get('dob')
        abc.PhnNo = request.POST.get('phn')
        abc.Password = request.POST.get('pw')
        abc.save()
        return redirect("/disp")
    else :
        context = {
            'a' : abc
        }
        return render(request, 'editPage.html', context)


#def index(request) : 
    #return HttpResponse("hello")
    #return render(request, 'hello.html', {'value':'5'})

def login(request) :
    if(request.method=='GET') :
       return render(request, 'hello.html')
    elif(request.method=='POST') :
        no1 = int(request.POST['num1'])
        no2 = int(request.POST.get('num2'))
        var = no1/no2
        print(var)
        #return render(request, 'hello.html')
        #return render(request, 'hi.html')
       #return render(request, 'home.html')

def operation(request) :
    if request.method == 'GET' :
        return render(request, 'hello.html')
    elif(request.method=='POST') :
        #Login.objects.create(UserName="Albin")
        no1 = int(request.POST['num1'])
        no2 = int(request.POST['num2'])
        var = str(no1/no2)
        return HttpResponse("The Quotient = " + var)   