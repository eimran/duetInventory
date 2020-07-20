from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="EmployeeHome"),
    # path('register', views.register, name='EmployeeRegister')
]
