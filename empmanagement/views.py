from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from .models import *
from .forms import EmployeeForm,DepartmentForm

import time

# Create your views here.
def homepage(request):
    time.sleep(1)
    
    return render(request,'user.html')

def custom_login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                
            
                return redirect('dashboard')  
                 
            else:
                messages.error(request, 'Invalid login credentials')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
def register(request):
   
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('adminsignin')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
def sidepanel(request):
    return render(request,'sidepanel.html')

def admindashboard(request):
    time.sleep(0.7)
    # Retrieve the count of rows for each model
    employee_count = Employee.objects.count()
    department_count = Department.objects.count()
    leave_count = Leave.objects.count()
    leave_request_rejected = LeaveRequest.objects.filter(status__exact="Rejected").count()
    approved_leave_aproved=LeaveRequest.objects.filter(status__exact="Approved").count()
    attendance_count = Attendance.objects.count()
    payroll_count = Payroll.objects.count()
    attendance_report_count = AttendanceReport.objects.count()

    # Pass the counts as context to the template
    context = {
        'employee_count': employee_count,
        'department_count': department_count,
        'leave_count': leave_count,
        'leave_request_rejected': leave_request_rejected,
        'attendance_count': attendance_count,
        'approved_leave_aproved': approved_leave_aproved,
        'attendance_report_count': attendance_report_count,
    }

    return render(request, 'Adminfiles/dashboard.html', context)

def admindepartment(request):
    time.sleep(0.7)
    departments = Department.objects.all()
    return render(request,'Adminfiles/departments.html',{'dept':departments})

def leave_management(request):
    time.sleep(1)
    leaves = Leave.objects.all()
    return render(request, 'Adminfiles/leave.html', {'leaves': leaves})


def add_leave(request):
    time.sleep(0.7)
    if request.method == "POST":
        leave_type = request.POST.get('leave_type')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Leave.objects.create(leave_type=leave_type, description=description, status=status)
        return redirect('leave_management')

    return render(request, 'Adminfiles/add_leave.html')

def update_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)

    if request.method == "POST":
        leave.leave_type = request.POST.get('leave_type')
        leave.description = request.POST.get('description')
        leave.status = request.POST.get('status')
        leave.save()
        return redirect('leave_management')

    return render(request, 'Adminfiles/update_leave.html', {'leave': leave})

def delete_leave(request, leave_id):
    leave = get_object_or_404(Leave, id=leave_id)
    leave.delete()
    return redirect('leave_management')


from django.shortcuts import render
from .models import Employee, Department
from django.db.models import Q
import time

def employee_summary(request):
    time.sleep(0.7)
    search_query = request.GET.get('search', '')
    department_filter = request.GET.get('department', '')
    
    employees = Employee.objects.all()
    
    if search_query:
        employees = employees.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
    
    if department_filter:
        employees = employees.filter(department_id=department_filter)
    
    departments = Department.objects.all()
    
    return render(request, 'Adminfiles/employee.html', {
        'employees': employees,
        'departments': departments,
    })

def attendance_list(request):
    time.sleep(0.7)
    
    attendances = Attendance.objects.select_related('employee').order_by('-date')[:10]
    return render(request, 'Adminfiles/attendance.html', {'attendances': attendances})
def attendance_all(request):
    time.sleep(0.7)
    
    attendances = Attendance.objects.select_related('employee').order_by('-date')
    return render(request, 'Adminfiles/all_attendance.html', {'attendances': attendances})
def attendance_report(request):
    # Fetching the attendance reports from the database
    attendance_reports = AttendanceReport.objects.all()
    
    # Passing the reports to the template
    return render(request, 'Adminfiles/attendance_report.html', {'attendance_reports': attendance_reports})
def attendance_report_add(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        total_days = request.POST.get('total_days')
        present_days = request.POST.get('present_days')
        absent_days = request.POST.get('absent_days')

        employee = Employee.objects.get(pk=employee_id) if employee_id else None

        AttendanceReport.objects.create(
            employee=employee,
            start_date=start_date,
            end_date=end_date,
            total_days=total_days,
            present_days=present_days,
            absent_days=absent_days
        )
        return redirect('attendance_report')

    employees = Employee.objects.all()
    return render(request, 'Adminfiles/attendance_report_add.html', {'employees': employees})

# Update attendance report
def attendance_report_update(request, pk):
    attendance_report = get_object_or_404(AttendanceReport, pk=pk)

    if request.method == "POST":
        attendance_report.employee_id = request.POST.get('employee')
        attendance_report.start_date = request.POST.get('start_date')
        attendance_report.end_date = request.POST.get('end_date')
        attendance_report.total_days = request.POST.get('total_days')
        attendance_report.present_days = request.POST.get('present_days')
        attendance_report.absent_days = request.POST.get('absent_days')
        attendance_report.save()
        return redirect('attendance_report')

    employees = Employee.objects.all()
    return render(request, 'Adminfiles/attendance_report_update.html', {'attendance_report': attendance_report, 'employees': employees})

# Delete attendance report
def attendance_report_delete(request, pk):
    attendance_report = get_object_or_404(AttendanceReport, pk=pk)

    if request.method == "POST":
        attendance_report.delete()
        return redirect('attendance_report')

    return render(request, 'Adminfiles/attendance_report_delete.html', {'attendance_report': attendance_report})
def leave_request(request):
    time.sleep(0.7)
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'Adminfiles/leave_request.html', {'leave_requests': leave_requests})

# View to approve a leave request
def approve_leave(request, request_id):
    leave_request = LeaveRequest.objects.get(id=request_id)
    leave_request.status = 'Approved'
    leave_request.save()
    return redirect('leave_request')  # Redirect back to the leave requests list

# View to reject a leave request
def reject_leave(request, request_id):
    time.sleep(0.3)
    leave_request = LeaveRequest.objects.get(id=request_id)
    leave_request.status = 'Rejected'
    leave_request.save()
    return redirect('leave_request')  
from django.contrib import messages

def update_department(request, pk):
    department = get_object_or_404(Department, pk=pk)

    if request.method == 'POST':
        department.name = request.POST.get('name')
        department.description = request.POST.get('description')
        department.save()
        messages.success(request, 'Department updated successfully!')
        return redirect('admindept')  

    return render(request, 'Adminfiles/update_dept.html', {'department': department})


    
def delete_department(request, pk):
    department = get_object_or_404(Department, pk=pk)
    
    if request.method == "POST":
        department.delete()
        return redirect('admindept')

    return render(request, 'Adminfiles/delete_dept.html', {'department': department})
def add_department(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department added successfully!')
            return redirect('admindept')  # Redirect to the list after adding
    else:
        form = DepartmentForm()

    return render(request, 'Adminfiles/add_dept.html', {'form': form})

def employee_update(request, pk):
    # Get the employee instance by pk
    employee = get_object_or_404(Employee, pk=pk)
    departments = Department.objects.all()

    if request.method == 'POST':
        # Pass the instance to the form for updating
        form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
            return redirect('employee_summary')

    else:
        # Pass the instance to the form for pre-populating data
        form = EmployeeForm(instance=employee)

    return render(request, 'Adminfiles/update_emp.html', {
        'form': form,
        'departments': departments,
    })

# Delete Employee (Without Forms)
def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == "POST":
        employee.delete()
        return redirect('employee_summary')
    
    return render(request, 'Adminfiles/delete_emp.html', {'employee': employee})
def employee_add(request):
    departments = Department.objects.all()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('employee_summary')

    else:
        form = EmployeeForm()

    return render(request, 'Adminfiles/employee_add.html', {
        'form': form,
        'departments': departments,
    })
def attendance_add(request):
    if request.method == "POST":
        employee_id = request.POST.get('employee')
        date = request.POST.get('date')
        status = request.POST.get('status')

        employee = Employee.objects.get(pk=employee_id) if employee_id else None

        Attendance.objects.create(
            employee=employee,
            date=date,
            status=status
        )
        return redirect('attendance_list')

    employees = Employee.objects.all()  # Fetch employees for dropdown
    return render(request, 'Adminfiles/add_attendance.html', {'employees': employees})

# Update attendance record
def attendance_update(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)

    if request.method == "POST":
        attendance.employee_id = request.POST.get('employee')
        attendance.date = request.POST.get('date')
        attendance.status = request.POST.get('status')
        attendance.save()
        return redirect('attendance_list')

    employees = Employee.objects.all()
    return render(request, 'Adminfiles/update_attendance.html', {'attendance': attendance, 'employees': employees})

# Delete attendance record
def attendance_delete(request, pk):
    attendance = get_object_or_404(Attendance, pk=pk)

    if request.method == "POST":
        attendance.delete()
        return redirect('attendance_list')

    return render(request, 'Adminfiles/del_attendance.html', {'attendance': attendance})


def userdashboard(request):
    return render(request,'Employeefiles/dashboard.html')