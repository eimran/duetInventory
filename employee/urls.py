from django.urls import path
from . import views

urlpatterns = [
    path("profile", views.index, name="profile"),
    # path('register', views.register, name='EmployeeRegister')
]

