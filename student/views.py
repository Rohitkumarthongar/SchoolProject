from datetime import datetime, time

from django.shortcuts import render



def fetch_list(request):
    student_data = { 'student_list' :{1:'Rohit',2:'Rajat',3:'Mishra',4:'Debnarayan'}}
    return render(request,'student.html',student_data)

# Create your views here.
def get_student_data(request):
    stu_name = "Rohit"
    roll_no = 45
    division = "10 th"
    date = datetime.now()

    stu_details = {'stu_name':stu_name,'roll_no':roll_no,'division':division,'d':date}

    # Using when it has single line of data
    # return render(request,'templates/student.html',context=stu_name)
    # use when it has more data
    return render(request,'student.html',stu_details)