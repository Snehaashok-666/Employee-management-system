from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('login/',views.custom_login,name='adminsignin'),
    path('signup/',views.register,name='adminsignup'),
    path('admindashboard',views.admindashboard,name='dashboard'),
    path('admindept',views.admindepartment,name='admindept'),
    path('leave-management/', views.leave_management, name='leave_management'),
    path('employee-summary/', views.employee_summary, name='employee_summary'),
    path('attendance/', views.attendance_list, name='attendance_list'),
    path('attendance_report/', views.attendance_report, name='attendance_report'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('approve_leave/<int:request_id>/', views.approve_leave, name='approve_leave'),
    path('reject_leave/<int:request_id>/', views.reject_leave, name='reject_leave'),
    path('departments/', views.Department, name='department_list'),
    path('departments/update/<int:pk>/',views. update_department, name='update_department'),
    path('departments/delete/<int:pk>/',views. delete_department, name='delete_department'),
    path('departments/add/',views. add_department, name='add_department'),
    path('employee/update/<int:pk>/', views.employee_update, name='employee_update'),
    path('employee/delete/<int:pk>/', views.employee_delete, name='employee_delete'),
    path('employee/add/', views.employee_add, name='employee_add'),
    path('attendance/add/', views.attendance_add, name='attendance_add'),
    path('attendance/update/<int:pk>/', views.attendance_update, name='attendance_update'),
    path('attendance/delete/<int:pk>/', views.attendance_delete, name='attendance_delete'),
    path('attendance_report/add/', views.attendance_report_add, name='attendance_report_add'),
    path('attendance_report/update/<int:pk>/', views.attendance_report_update, name='attendance_report_update'),
    path('attendance_report/delete/<int:pk>/', views.attendance_report_delete, name='attendance_report_delete'),
    path('sidepanel',views.sidepanel,name='sidepanel'),
    path('empdash/',views.userdashboard,name='user_dashboard'),
    path('leave-management/add/', views.add_leave, name='add_leave'),
    path('leave-management/update/<int:leave_id>/', views.update_leave, name='update_leave'),
    path('leave-management/delete/<int:leave_id>/', views.delete_leave, name='delete_leave'),
    path('allattendances/',views.attendance_all,name='attendance_all')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)