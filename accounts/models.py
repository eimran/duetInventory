from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

from employee.models import Employee


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, employee=0):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            employee=employee,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, employee):
        find_emp = Employee.objects.get(pk=employee)
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            employee=employee,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", help_text='Required. Add a valid email address', max_length=60,
                              unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'employee']

    objects = MyAccountManager()

    def __str__(self):
        return self.username + self.employee.employee_no


def has_perm(self, perm, obj=None):
    return self.is_admin


def has_module_perms(self, app_label):
    return self.is_superuser
