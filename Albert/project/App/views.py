from django.shortcuts import render,redirect

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from App.models import*
from App.form import*


# Create your views here.
def home(request):
    return render(request,'home.html')
def mainpage(request):
    return render(request,'mainpage.html')
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('pass1')
        password2=request.POST.get('cpass1')
        if password1==password2:
            if User.objects.filter(username=username,email=email).exists():
                    messages.info(request,'username already exists')
                    print("Already Have")
            else:
                new_user=User.objects.create_user(username,email,password1)
                new_user.save()
                print('success')
                return redirect(user_login)
        else:
            print("wrong password")
    return render(request,'signup.html')
def user_login(request):
    if request.method=='POST':
        Username=request.POST.get('username')
        password1=request.POST.get('pass1')
        user=authenticate(request,username=Username,password=password1)
        if user is not None:
            login(request,user)
            return redirect(mainpage)
        else:
            messages.info(request,'user not exist')
            print('user not exist')
            return redirect(user_login)
    return render(request,'login.html')
        

def user_logout(request):
    logout(request)
    return redirect(user_login)
def add_book(request):
    #  form=bookform()
     if(request.method=='POST'):
          d=bookform(request.POST)
          if d.is_valid():
            d.save()
            return redirect(view_book)
     return render (request,'add_book.html')
def view_book(request):
    b=book.objects.all()
    return render (request,'list.html',{'book':b})
def list(request):
    content=book.objects.all()
    data={
        'result':content
    }
    return render(request,'list.html',data)
