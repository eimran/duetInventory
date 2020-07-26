from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.index, name="profile"),
    path('employee-add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('employee/delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path("employee-list", views.employee_list, name="employee_list"),
    path('employee/edit/<int:pk>', views.EmployeeUpdateView.as_view(), name='update_employee'),
    # path('employee/edit/<int:pk>', views.employee_update_view, name='update_employee'),

    path('work-record-add/', views.WorkRecordCreateView.as_view(), name='work_record_add'),
    path('work-record/delete/<int:pk>', views.WorkRecordDeleteView.as_view(), name='work_record_delete'),
    path("work-record-list", views.work_record_list, name="work_record_list"),
    path('work-record/edit/<int:pk>', views.WorkRecordUpdateView.as_view(), name='work_record_update'),

    path('dept-add/', views.DeptCreateView.as_view(), name='dept_add'),
    path('dept/delete/<int:pk>', views.DeptDeleteView.as_view(), name='dept_delete'),
    path("dept-list", views.dept_list, name="dept_list"),
    path('dept/edit/<int:pk>', views.DeptUpdateView.as_view(), name='dept_update'),

    path('faculty-add/', views.FacultyCreateView.as_view(), name='faculty_add'),
    path('faculty/delete/<int:pk>', views.FacultyDeleteView.as_view(), name='faculty_delete'),
    path("faculty-list", views.faculty_list, name="faculty_list"),
    path('faculty/edit/<int:pk>', views.FacultyUpdateView.as_view(), name='faculty_update'),
    # path('register', views.register, name='EmployeeRegister')
]

