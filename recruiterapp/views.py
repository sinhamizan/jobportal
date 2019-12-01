from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth.models import auth, User
from django.contrib import messages

# Create your views here.

def recruiterRegister(request):
    if request.method == 'POST':
        user = request.POST['username'],
        first_name = request.POST['compname'],
        last_name = request.POST['compaddr'],
        password1 = request.POST['password'],
        password2 = request.POST['conpass']

        if password1 == password2:
            if User.objects.filter(username=user).exists():
                messages.info(request, 'user taken !')
            else:
                user = User.objects.create_user(username=user, password=password1, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'password no mathig !')
            
    return render(request, 'recruiter_register.html')


def recruiterLogin(request):
    if request.method == 'POST':
        user = request.POST['username'],
        passw = request.POST['password']

        user = auth.authenticate(username=user, password=passw)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid !')
            return redirect('recruiter_login')
    else:
        return render(request, 'rec_login.html')




