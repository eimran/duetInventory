from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    #path('', views.home, name="home"),
    path('user_register', views.user_register, name="user_register"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
    path("password_reset", views.password_reset, name="password_reset")
]
