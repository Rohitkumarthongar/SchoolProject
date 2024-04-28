from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return HttpResponse('Hello Jaipur Govindgarh')

def learn_python(request):
    return HttpResponse('<H1>Hello G</H1>')

def learn_py(request):
    a = '<H1>Hello G</H1>'
    b =  "Hello this is Rohit Kumar soni "
    return HttpResponse(a+b)

def index(request):
    return render(request,"homepage.html")