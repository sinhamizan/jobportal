from django.urls import path
from . import views

urlpatterns = [
    path('recruiter-register/', views.recruiterRegister, name="recruiter_register"),
    path('recruiter-login/', views.recruiterLogin, name="recruiter_login"),
]
