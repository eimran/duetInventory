from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    #path('', views.home, name="home"),
    path("login", views.login_view, name="login"),
    path("user_register", views.registration_view, name="registration_view"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout_view, name="logout"),
    path("password_reset", views.password_reset, name="password_reset")
]
