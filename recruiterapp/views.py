from django.shortcuts import render
from .models import Category

# Create your views here.

def recruiterRegister(request):

    return render(request, 'recruiter_register.html')



