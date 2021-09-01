from django.db.models import fields
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import Form, ModelForm, DateField, widgets
from .models import Attendance, Employee, Status, DateAndTime, Designation




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class addEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class addAttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
        widgets = {
                'date_created': widgets.DateTimeInput(attrs={'type': 'datetime-local'})
        }   

class addStatusForm(ModelForm):
    class Meta:
        model = Status
        fields = '__all__'   

class addDateAndTimeForm(ModelForm):
    class Meta:
        model = DateAndTime
        fields = '__all__' 
        widgets = {
                'date': widgets.DateInput(attrs={'type': 'date'})
        }

class addDesignationForm(ModelForm):
    class Meta:
        model = Designation
        fields = '__all__'     