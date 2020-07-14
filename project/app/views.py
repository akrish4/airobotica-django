from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Contact
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('num')
        desc=request.POST.get('desc')
        myusercontact=Contact(name=name,email=email,phone=phone,desc=desc)
        myusercontact.save()
        messages.warning(request,"Your Response has been recorded")
        return redirect('/')

    return render(request,'contact.html')

def handleSignup(request):
    if request.method == 'POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 != pass2:
            return HttpResponse("password is not matching")
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        return HttpResponse("Signup Successful")

    return render(request,'signup.html')  

def handleLogin(request):

    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,"Login SuccessFull")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/login")    

    return render(request,'login.html')    

def friends(request):
    return render(request,'friends.html')  



def handleBlog(request):
    return render(request,'handleblog.html') 



def about(request):
    return render(request,'about.html')      