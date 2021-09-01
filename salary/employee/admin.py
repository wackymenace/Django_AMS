from django.contrib import admin
from .models import *
from ims.models import *
# Register your models here.
registeredSites = [
    Employee,
    Designation,
    Attendance,
    Status,
    DateAndTime,

    Unit,
    Item,
    ItemType,
    Invoice,
]

admin.site.register(registeredSites)