from django.db import models

# Department Model: to store department details
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

# Employee Model: to store employee details
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    date_of_joining = models.DateField()
    date_of_birth = models.DateField()
    address = models.TextField()
   
    designation = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    





# Leave Model: to store leave types (like Casual Leave, Sick Leave)
class Leave(models.Model):
    leave_type = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')

    def __str__(self):
        return self.leave_type

# LeaveRequest Model: for employees to request leave
class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(Leave, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"Leave Request for {self.employee} from {self.start_date} to {self.end_date}"

# Attendance Model: to track daily attendance
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Leave', 'Leave')], default='Absent')

    def __str__(self):
        return f"Attendance for {self.employee} on {self.date}"

# Payroll Model: to store payroll data for employees
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pay_date = models.DateField()

    def __str__(self):
        return f"Payroll for {self.employee} on {self.pay_date}"

# AttendanceReport Model: to generate reports for attendance
class AttendanceReport(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.IntegerField()
    present_days = models.IntegerField()
    absent_days = models.IntegerField()

    def __str__(self):
        return f"Attendance Report for {self.employee} from {self.start_date} to {self.end_date}"

