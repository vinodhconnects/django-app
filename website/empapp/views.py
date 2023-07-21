from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
# Create your views here.

def app_home(request):
    employees = Employee.objects.all()  #returns QuerySet

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    form = EmployeeForm()
    context = {
        'employees': employees,
        'name':'Employees',
         'form':form
    }
    
    return render(request,'employee.html', context)