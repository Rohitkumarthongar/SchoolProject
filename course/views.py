from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def get_course_list(request):
    return HttpResponse("REcive the Course List")

def create_course(request):
    return HttpResponse("Course HAs Been Added To List")

def update_course_list(request):
    return HttpResponse('Course LIst has Been Updated')

def index(request):
    return render(request,'course html/course.html')