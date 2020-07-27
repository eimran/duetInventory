import django_filters
from .models import *


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'cell_no', 'email', 'employee_no')