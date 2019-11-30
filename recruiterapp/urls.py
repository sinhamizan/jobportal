from django.urls import path
from . import views

urlpatterns = [
    path('recruiter-register/', views.recruiterRegister, name="recruiter_register"),
]
