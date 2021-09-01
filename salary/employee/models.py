from django.db.models.base import Model
import employee
from django.db import models
from django.db.models.deletion import CASCADE
import datetime


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=100, default="Employee Name")
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12, default="Phone Number")
    designation = models.ManyToManyField('Designation')
    salary = models.IntegerField(default=10000)
    cnic = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=254, null=True)

    def __str__(self):
        return self.first_name


class Designation(models.Model):
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


class DateAndTime(models.Model):
    
    month_choices = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    month = models.CharField(max_length=100, choices=month_choices, default='January')

    def __str__(self):
        return self.month



class Status(models.Model):
    attendance_choice = models.CharField(max_length=100, default='Present')
    def __str__(self):
        return self.attendance_choice



class Attendance(models.Model):
    day_choices = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )
    day = models.CharField(max_length=100, default=datetime.datetime.today().strftime("%A"), choices=day_choices)

    month_choices = (
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )
    month = models.CharField(max_length=100, default=datetime.datetime.today().strftime("%B"), choices=month_choices)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(null=True, default=datetime.datetime.now())

    def __str__(self):
        return u"%s %s %s" %(self.employee, self.status, self.date_created)