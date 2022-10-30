from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('newpage')

        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,"login.html")


def newpage(request):
    return render(request,'newpage.html')

def form(request):
    return render(request,'form.html')

def messagepage(request):
    if request.method == 'POST':
        name = request.POST['name']
        DOB = request.POST['DOB']
        age = request.POST['age']
        email = request.POST['email']
        branch = request.POST['branch']
        return render(request,'messagepage.html',{'name':name,'DOB':DOB,'age':age,'email':email,'branch':branch})


def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name already taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')

    return render(request,"register.html")
