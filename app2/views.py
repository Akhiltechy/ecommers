from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login(request):
    if request.method == "POST":
        y1 = request.POST['m1']
        y2 = request.POST['m2']
        user=auth.authenticate(username=y1,password=y2)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invaild username or password')
            return redirect('login')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        x1 = request.POST['n1']
        x2 = request.POST['n2']
        x3 = request.POST['n3']
        x4 = request.POST['n4']
        x5 = request.POST['n5']
        x6 = request.POST['n6']
        if x5 == x6:
            if User.objects.filter(username=x1).exists():
                messages.info(request, 'USERNAME ALREADY TAKEN')
                return redirect('register')

            if User.objects.filter(email=x4).exists():
                messages.info(request, 'EMAIL ALREADY TAKEN')
                return redirect('register')

            else:
                user = User.objects.create_user(username=x1, first_name=x2, last_name=x3, email=x4, password=x5)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'PASSWORD INCORRECT')
            return redirect('register')

    return render(request, 'register.html')
