"""schoolproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

import course
from result import views as rslt
from registration import views as reg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pytho/',rslt.learn_python),
    path('py/',rslt.learn_py),
    path('django/',rslt.learn_django),
    path('',rslt.index),

    path('regis/',include([
         path('registration/',reg.register_student),
         path('registration_update/', reg.update_student_profile),
         path('',reg.index)
    ])),

    path('crs/',include('course.urls')),
    path('stud/',include('student.urls')),
    path('staff/',include('staff_details.urls')),

]
