from django.contrib.auth import login
from django.urls import path
from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LoginPage, name='login'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.RegisterPage, name="register"),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('details/<int:pk>', views.EmployeeDetails),
    path('user/', views.User),
    path('details/', views.Details),
    path('ims/', include('ims.urls')),

    path('addEmployee/', views.CreateEmployee),
    path('updateEmployee/<str:pk>', views.UpdateEmployee),
    path('deleteEmployee/<str:pk>', views.deleteEmployee),
    
    path('addStatus/', views.CreateStatus),
    path('updateStatus/<int:pk>', views.UpdateStatus),
    path('deleteStatus/<int:pk>', views.deleteStatus),

    path('addAttendance/', views.CreateAttendance),
    path('updateAttendance/<int:pk>', views.UpdateAttendance),
    path('deleteAttendance/<int:pk>', views.deleteAttendance),

    path('addDesignation/', views.CreateDesignation),
    path('updateDesignation/<int:pk>', views.UpdateDesignation),
    path('deleteDesignation/<int:pk>', views.deleteDesignation),

    path('addDateAndTime/', views.CreateDateAndTime),
    path('updateDateAndTime/<int:pk>', views.UpdateDateAndTime),
    path('deleteDateAndTime/<int:pk>', views.deleteDateAndTime),

    path('payslip/<int:pk>', views.Payslip),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
