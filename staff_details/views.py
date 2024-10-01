from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def get_employee_detals(request):
    return HttpResponse('Now Employee Detals PAge Is Working ')

def fetch_employee_list(request):
    return render(request, 'staff_details/staff_details.html')
