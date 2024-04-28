from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def update_student_profile(request):
    return HttpResponse("Profile Updated")

def register_student(request):
    return HttpResponse('Registration Succesfully ')

def index(request):
    return render(request,'registration html/registration.html')