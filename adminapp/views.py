from django.shortcuts import render
from .models import Category

# Create your views here.

def home(request):
    cat = Category.objects.all()
    context = {
        'cat':cat,
    }
    return render(request, 'home.html', context)


def jobs(request):
    return render(request, 'jobs.html')

