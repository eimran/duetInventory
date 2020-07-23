from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.index, name="profile"),
    path('employee-add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('employee/delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path("employee-list", views.employee_list, name="employee_list"),
    path('employee/edit/<int:pk>', views.EmployeeUpdateView.as_view(), name='update_employee'),
    # path('register', views.register, name='EmployeeRegister')
]

