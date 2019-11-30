from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('recruiter-register/', views.recruiterRegister, name="recruiter_register"),
]
