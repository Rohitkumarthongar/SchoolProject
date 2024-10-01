from django.urls import path
from staff_details import views

urlpatterns=[
    path('get/',views.get_employee_detals),
    path('fetch/',views.fetch_employee_list)
]