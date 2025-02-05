from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Employee
from datetime import date, timedelta

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User  # Using Django's default User model
        fields = ["username", "first_name", "email", "password1", "password2"]

    def clean_email(self):
        """Ensure email is unique."""
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email

    def save(self, commit=True):
        """Save the user with additional fields."""
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]  # Change from name → first_name
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

from .models import Department

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']



from datetime import date, timedelta
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), required=True)
    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'email', 'phone_number', 'department',
            'date_of_joining', 'date_of_birth', 'address', 'designation'
        ]

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError("First name should only contain letters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError("Last name should only contain letters.")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Employee.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or not (10 <= len(phone_number) <= 15):
            raise forms.ValidationError("Enter a valid phone number (10-15 digits).")
        return phone_number

    def clean_date_of_joining(self):
        date_of_joining = self.cleaned_data.get('date_of_joining')
        if date_of_joining > date.today():
            raise forms.ValidationError("Date of joining cannot be in the future.")
        return date_of_joining

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        date_of_joining = self.cleaned_data.get('date_of_joining')

        if date_of_birth >= date.today():
            raise forms.ValidationError("Date of birth cannot be today or in the future.")

        if date_of_joining:
            min_birth_date = date_of_joining - timedelta(days=18 * 365)  # Roughly 18 years
            if date_of_birth > min_birth_date:
                raise forms.ValidationError("Employee must be at least 18 years old at the time of joining.")

        return date_of_birth

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if len(address) < 10:
            raise forms.ValidationError("Address must be at least 10 characters long.")
        return address

    def clean_designation(self):
        designation = self.cleaned_data.get('designation')
        if not designation.strip():
            raise forms.ValidationError("Designation cannot be empty.")
        return designation

