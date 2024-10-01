from django.urls import path
from student import views

urlpatterns=[
    path('get/',views.get_student_data),
    path('fetch/',views.fetch_list)
]