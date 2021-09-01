from django.db.models import query
import employee
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from .filters import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Username OR Password is Incorrect')
                return render(request, 'employee/Login/Login.html')

        context = {}
        return render(request, 'employee/Login/Login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for' + user)
                return redirect('login')

    context = {'form': form}
    return render(request, 'employee/Login/register.html', context)

@login_required(login_url='login')
def EmployeeDetails(request, pk):
    employeeS = Employee.objects.get(id=pk)
    attendances = Attendance.objects.filter(employee__id__contains=pk)
    present = Attendance.objects.filter(
        status__attendance_choice__contains='Present', employee__id__contains=pk).count()
    presentMonth = Attendance.objects.filter(
        status__attendance_choice__contains='Present', employee__id__contains=pk, month__contains=datetime.datetime.today().strftime("%B")).count()
    absent = Attendance.objects.filter(
        status__attendance_choice__contains='absent', employee__id__contains=pk).count()
    leave = Attendance.objects.filter(
        status__attendance_choice__contains='leave', employee__id__contains=pk).count()
    halfTime = Attendance.objects.filter(
        status__attendance_choice__contains='halfTime', employee__id__contains=pk).count()
    attendanceFilter = AttendanceFilter(request.GET, queryset=attendances)
    attendances = attendanceFilter.qs
    attendancesCount = attendanceFilter.qs.count()
    salary = employeeS.salary
    TemporaryVar = salary/30
    TemporaryVar2 = TemporaryVar/2
    TemporaryVar3 = TemporaryVar * absent
    TemporaryVar4 = TemporaryVar2 * halfTime
    TemporaryVar5 = present * TemporaryVar
    #Tsalary = TemporaryVar5
    TemporaryVar6 = 1000
    Tsalary = salary - (TemporaryVar3 + TemporaryVar4)

    if absent > 10:
        perfomance = "Bad!"

    if absent < 10 and absent > 5:
        perfomance = "Better!"

    if absent < 5 and absent > 3:
        perfomance = "Good!"

    if absent < 3:
        perfomance = "Awesome!"

    context = {
        'employee': employeeS,
        'present': present,
        'presentMonth':presentMonth,
        'absent': absent,
        'leave': leave,
        'halfTime': halfTime,
        'Tsalary': Tsalary,
        'perfomance': perfomance,
        'attendances':attendances,
        'attendanceCount':attendancesCount,
        'attendanceFilter':attendanceFilter,
    }
    return render(request, 'employee/Employee/employee_details.html', context)

@login_required(login_url='login')
def Payslip(request, pk):
    attendance = Attendance.objects.all()
    designation = Designation.objects.all()
    employeeS = Employee.objects.get(id=pk)
    present = Attendance.objects.filter(
        status__attendance_choice__contains='Present', employee__id__contains=pk).count()
    absent = Attendance.objects.filter(
        status__attendance_choice__contains='absent', employee__id__contains=pk).count()
    leave = Attendance.objects.filter(
        status__attendance_choice__contains='leave', employee__id__contains=pk).count()
    halfTime = Attendance.objects.filter(
        status__attendance_choice__contains='halfTime', employee__id__contains=pk).count()
    salary = employeeS.salary
    TemporaryVar = salary/30
    TemporaryVar2 = TemporaryVar/2
    TemporaryVar3 = TemporaryVar * absent
    TemporaryVar4 = TemporaryVar2 * halfTime
    TemporaryVar5 = present * TemporaryVar
    Tsalary = round(TemporaryVar5, 1)
    daysWorked = present+absent+halfTime
    TemporaryVar6 = 1000
    TemporaryVar7 = TemporaryVar3 + TemporaryVar4
    #Tsalary = salary - (TemporaryVar3 + TemporaryVar4)

    if absent > 10:
        perfomance = "Bad!"

    if absent < 10 and absent > 5:
        perfomance = "Better!"

    if absent < 5 and absent > 3:
        perfomance = "Good!"

    if absent < 3:
        perfomance = "Awesome!"

    context = {
        'employee': employeeS,
        'present': present,
        'absent': absent,
        'leave': leave,
        'leave2': TemporaryVar4,
        'halfTime': halfTime,
        'Tsalary': Tsalary,
        'perfomance': perfomance,
        'attendance': attendance,
        'designation': designation,
        'daysWorked': daysWorked,
        'TemporaryVar7': TemporaryVar7,
    }
    return render(request, 'employee/payslip.html', context)


@login_required(login_url='login')
def Dashboard(request):
    employees = Employee.objects.all()
    employeesCount = Employee.objects.all().count()
    attendance = Attendance.objects.all().order_by('-date_created')[:employeesCount:1]
    attendanceCount = Attendance.objects.all().count()
    context = {
        'employees': employees,
        'attendances': attendance,
        'attendanceCount': attendanceCount,
    }
    return render(request, 'employee/dashboard.html', context)

@login_required(login_url='login')
def Details(request):
    employees = Employee.objects.all()
    attendances = Attendance.objects.all()
    attendancesCountTotal = Attendance.objects.all().count()
    statuses = Status.objects.all()
    designations = Designation.objects.all()
    dateandtime = DateAndTime.objects.all()
    employeeFilter = EmployeeFilter(request.GET, queryset=employees)
    employees = employeeFilter.qs
    attendanceFilter = AttendanceFilter(request.GET, queryset=attendances)
    attendances = attendanceFilter.qs
    attendancesCount = attendanceFilter.qs.count()
    context = {
        'attendanceFilter': attendanceFilter,
        'employeeFilter': employeeFilter,
        'employees': employees,
        'attendances': attendances,
        'statuses': statuses,
        'designations': designations,
        'dateandtime': dateandtime,
        'attendancesCount': attendancesCount,
        'attendancesCountTotal': attendancesCountTotal,
    }
    return render(request, 'employee/tables.html', context)

@login_required(login_url='login')
def User(request):
    return render(request, 'employee/user.html')

@login_required(login_url='login')
def CreateEmployee(request):
    form = addEmployeeForm()
    if request.method == 'POST':
        form = addEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'employee/Employee/add_employee.html', context)

@login_required(login_url='login')
def UpdateEmployee(request, pk):
    status = Employee.objects.get(id=pk)
    form = addEmployeeForm(instance=status)
    if request.method == 'POST':
        form = addEmployeeForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('/details')

    context = {'form': form}
    return render(request, 'employee/Employee/update_employee.html', context)

@login_required(login_url='login')
def deleteEmployee(request, pk):
    status = Employee.objects.get(id=pk)
    if request.method == "POST":
        status.delete()
        return redirect('/details/')

    context = {'employee': status}
    return render(request, 'employee/Employee/delete_employee.html', context)


@login_required(login_url='login')
def CreateStatus(request):
    form = addStatusForm()
    if request.method == 'POST':
        form = addStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/details')

    context = {'form': form}
    return render(request, 'employee/Status/add_status.html', context)

@login_required(login_url='login')
def UpdateStatus(request, pk):
    status = Status.objects.get(id=pk)
    form = addStatusForm(instance=status)
    if request.method == 'POST':
        form = addStatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('/details')

    context = {'form': form}
    return render(request, 'employee/Status/update_status.html', context)

@login_required(login_url='login')
def deleteStatus(request, pk):
    status = Status.objects.get(id=pk)
    if request.method == "POST":
        status.delete()
        return redirect('/details/')

    context = {'employee': status}
    return render(request, 'employee/Status/delete_status.html', context)


# Attendance
@login_required(login_url='login')
def CreateAttendance(request):
    form = addAttendanceForm()
    if request.method == 'POST':
        form = addAttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/details')

    context = {'form': form}
    return render(request, 'employee/Attendance/addAttendance.html', context)

@login_required(login_url='login')
def UpdateAttendance(request, pk):
    status = Attendance.objects.get(id=pk)
    form = addAttendanceForm(instance=status)
    if request.method == 'POST':
        form = addAttendanceForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('/details')

    context = {'form': form}
    return render(request, 'employee/Attendance/updateAttendance.html', context)

@login_required(login_url='login')
def deleteAttendance(request, pk):
    status = Attendance.objects.get(id=pk)
    if request.method == "POST":
        status.delete()
        return redirect('/details/')

    context = {'employee': status}
    return render(request, 'employee/Attendance/deleteAttendance.html', context)


# Designation
@login_required(login_url='login')
def CreateDesignation(request):
    form = addDesignationForm()
    if request.method == 'POST':
        form = addDesignationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/details')

    context = {'form': form}
    return render(request, 'employee/Designation/addDesignation.html', context)

@login_required(login_url='login')
def UpdateDesignation(request, pk):
    status = Designation.objects.get(id=pk)
    form = addDesignationForm(instance=status)
    if request.method == 'POST':
        form = addDesignationForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('/details')

    context = {'form': form}
    return render(request, 'employee/Designation/updateDesignation.html', context)

@login_required(login_url='login')
def deleteDesignation(request, pk):
    status = Designation.objects.get(id=pk)
    if request.method == "POST":
        status.delete()
        return redirect('/details/')

    context = {'employee': status}
    return render(request, 'employee/Designation/deleteDesignation.html', context)


# Date And time
@login_required(login_url='login')
def CreateDateAndTime(request):
    form = addDateAndTimeForm()
    if request.method == 'POST':
        form = addDateAndTimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/details')

    context = {'form': form}
    return render(request, 'employee/DateAndTime/addDateAndTime.html', context)

@login_required(login_url='login')
def UpdateDateAndTime(request, pk):
    status = DateAndTime.objects.get(id=pk)
    form = addDateAndTimeForm(instance=status)
    if request.method == 'POST':
        form = addDateAndTimeForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            return redirect('/details')

    context = {'form': form}
    return render(request, 'employee/DateAndTime/updateDateAndTime.html', context)

@login_required(login_url='login')
def deleteDateAndTime(request, pk):
    status = DateAndTime.objects.get(id=pk)
    if request.method == "POST":
        status.delete()
        return redirect('/details/')

    context = {'employee': status}
    return render(request, 'employee/DateAndTime/deleteDateAndTime.html', context)
