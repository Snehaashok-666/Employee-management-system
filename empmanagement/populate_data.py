from datetime import date
from .models import Department, Employee  

# Create 5 random departments
departments = [
    "HR", "Sales", "IT", "Marketing", "Finance", 
    "Research & Development", "Customer Support", "Operations", "Legal", "Admin"
]

# Insert the departments into the database
for dept in departments:
    Department.objects.create(name=dept, description=f"This is the {dept} department.")

# Create 20 random employees
employees = [
    ("John", "Doe", "john.doe@example.com", "1234567890", "Manager", "HR"),
    ("Jane", "Smith", "jane.smith@example.com", "2345678901", "Developer", "IT"),
    ("Alice", "Johnson", "alice.johnson@example.com", "3456789012", "Designer", "Marketing"),
    ("Bob", "Brown", "bob.brown@example.com", "4567890123", "Accountant", "Finance"),
    ("Charlie", "Davis", "charlie.davis@example.com", "5678901234", "Consultant", "Operations"),
    ("Eve", "Martinez", "eve.martinez@example.com", "6789012345", "Sales Manager", "Sales"),
    ("Frank", "Lopez", "frank.lopez@example.com", "7890123456", "Legal Advisor", "Legal"),
    ("Grace", "Wilson", "grace.wilson@example.com", "8901234567", "HR Specialist", "HR"),
    ("Hank", "Moore", "hank.moore@example.com", "9012345678", "Product Manager", "Marketing"),
    ("Ivy", "Taylor", "ivy.taylor@example.com", "1234567891", "Developer", "IT"),
    ("Jack", "Anderson", "jack.anderson@example.com", "2345678902", "Operations Lead", "Operations"),
    ("Kathy", "Thomas", "kathy.thomas@example.com", "3456789013", "Customer Support", "Customer Support"),
    ("Leo", "Jackson", "leo.jackson@example.com", "4567890124", "Data Analyst", "Research & Development"),
    ("Mona", "White", "mona.white@example.com", "5678901235", "Marketing Specialist", "Marketing"),
    ("Nick", "Harris", "nick.harris@example.com", "6789012346", "Finance Manager", "Finance"),
    ("Olivia", "Martinez", "olivia.martinez@example.com", "7890123457", "Customer Support", "Customer Support"),
    ("Paul", "Garcia", "paul.garcia@example.com", "8901234568", "Admin Assistant", "Admin"),
    ("Quincy", "Rodriguez", "quincy.rodriguez@example.com", "9012345679", "Project Manager", "Operations"),
    ("Rachel", "Martinez", "rachel.martinez@example.com", "1234567892", "Sales Representative", "Sales"),
    ("Samuel", "Perez", "samuel.perez@example.com", "2345678903", "Legal Assistant", "Legal")
]

# Insert employees into the database
for emp in employees:
    department = Department.objects.get(name=emp[5])
    Employee.objects.create(
        first_name=emp[0],
        last_name=emp[1],
        email=emp[2],
        phone_number=emp[3],
        designation=emp[4],
        department=department,
        date_of_joining=date.today(),
        date_of_birth="1990-01-01",  # Set a default date of birth
        address="1234 Example St, City, Country",  # Set a default address
    )
from empmanagement.models import Department, Employee, Leave, LeaveRequest, Attendance, Payroll, AttendanceReport
from datetime import date, timedelta

# Create Leave Types
leave_types = [
    "Sick Leave",
    "Casual Leave",
    "Paid Leave",
    "Unpaid Leave",
    "Maternity Leave"
]

for leave_type in leave_types:
    Leave.objects.get_or_create(leave_type=leave_type, description=f"Description for {leave_type}")

# Assuming some employees exist
employees = Employee.objects.all()

# Create Leave Requests
for employee in employees:
    leave_type = Leave.objects.get(leave_type="Sick Leave")
    LeaveRequest.objects.create(
        employee=employee,
        leave_type=leave_type,
        start_date=date.today() - timedelta(days=5),
        end_date=date.today() - timedelta(days=3),
        status="Approved"
    )
    LeaveRequest.objects.create(
        employee=employee,
        leave_type=leave_type,
        start_date=date.today() - timedelta(days=10),
        end_date=date.today() - timedelta(days=8),
        status="Pending"
    )

# Create Attendance Records
for employee in employees:
    for i in range(1, 11):  # Creating attendance for 10 days
        Attendance.objects.create(
            employee=employee,
            date=date.today() - timedelta(days=i),
            status="Present" if i % 2 == 0 else "Absent"
        )

# Create Payroll Entries
for employee in employees:
    Payroll.objects.create(
        employee=employee,
        salary=5000.00,
        bonus=500.00,
        deductions=200.00,
        pay_date=date.today().replace(day=28)  # Assuming payday is on the 28th of each month
    )

# Create Attendance Reports
for employee in employees:
    total_days = 10
    present_days = 6
    absent_days = total_days - present_days
    AttendanceReport.objects.create(
        employee=employee,
        start_date=date.today() - timedelta(days=9),
        end_date=date.today(),
        total_days=total_days,
        present_days=present_days,
        absent_days=absent_days
    )

print("Dummy data added successfully!")
