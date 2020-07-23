from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Employee
from .forms import EmployeeUpdateForm
from django.views.generic import CreateView, UpdateView, DeleteView, FormView


def index(request):
    return render(request, 'employee/employee_profile.html')


def employee_list(request):
    employees = Employee.objects.order_by('id').all()
    context = {'employees': employees}
    return render(request, 'employee/employee_list.html', context)


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee/employee_update.html'
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy('profile')
    #fields = ['category_name', 'details', 'parent_id']