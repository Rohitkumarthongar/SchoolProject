from django.urls import path
from course import views

urlpatterns=[
    path('create/',views.create_course),
    path('get/',views.get_course_list),
    path('update/',views.update_course_list),
    path('',views.index)
]