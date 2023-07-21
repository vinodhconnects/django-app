from django.shortcuts import render
from .models import Employee

# Create your views here.

def app_home(request):
    employees = Employee.objects.all()  #returns QuerySet

 
    context = {
        'employees': employees,
        'name':'Employees'
    }
    
    return render(request,'employee.html', context)