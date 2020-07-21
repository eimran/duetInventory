from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    # path('user-register/', views.user_register, name="user_register"),
    path('user-register/', views.registration_view, name="user_register"),
    path("login/", views.login_view, name="login"),
    path("account/", views.account_view, name="account"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout_view, name="logout"),
    # path("password_reset", views.password_reset, name="password_reset"),

# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/registration/password_change_done.html'),
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/registration/password_change.html'),
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/registration/password_reset_complete.html'),
     name='password_reset_complete'),
]