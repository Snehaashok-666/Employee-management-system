from django.contrib import admin
from .models import Department, Employee, Leave, LeaveRequest, Attendance, Payroll, AttendanceReport

# Registering Department model
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

# Registering Employee model
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'department', 'date_of_joining', 'date_of_birth')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('department', 'date_of_joining')

# Registering Leave model
@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('leave_type', 'description')
    search_fields = ('leave_type',)

# Registering LeaveRequest model
@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'leave_type', 'start_date', 'end_date', 'status')
    search_fields = ('employee__first_name', 'employee__last_name', 'leave_type__leave_type')
    list_filter = ('status', 'leave_type')

# Registering Attendance model
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('status', 'employee')

# Registering Payroll model
@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary', 'bonus', 'deductions', 'pay_date')
    search_fields = ('employee__first_name', 'employee__last_name')
    list_filter = ('pay_date',)

# Registering AttendanceReport model
@admin.register(AttendanceReport)
class AttendanceReportAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'total_days', 'present_days', 'absent_days')
    search_fields = ('employee__first_name', 'employee__last_name')
    list_filter = ('start_date', 'end_date')
