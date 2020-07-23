from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Employee, Department, Faculty
from .forms import EmployeeUpdateForm, EmployeeCreateForm, DeptCreateForm, DeptUpdateForm, FacultyCreateForm, FacultyUpdateForm
from django.views.generic import CreateView, UpdateView, DeleteView, FormView


def index(request):
    return render(request, 'employee/employee_profile.html')


class EmployeeCreateView(CreateView):
    template_name = 'product/product/product_add.html'
    form_class = EmployeeCreateForm

    def post(self, request, *args, **kwargs):
        form = EmployeeCreateForm(request.POST)
        if form.is_valid():
            employee = form.save()
            employee.created_by = request.user
            employee.active_status = 1
            employee.category = 't'
            employee.save()
            # return HttpResponseRedirect(reverse_lazy('products:detail', args=[product.id]))
            messages.info(request, 'Employee Added')
        # return render(request, 'employee/employee_list.html', {'form': form})
        return redirect('employee_list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee/employee_delete.html'
    success_url = reverse_lazy('employee_list')


def employee_list(request):
    employees = Employee.objects.order_by('id').all()
    context = {'employees': employees}
    return render(request, 'employee/employee_list.html', context)


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee/employee_update.html'
    form_class = EmployeeUpdateForm
    success_url = reverse_lazy('profile')


class DeptCreateView(CreateView):
    template_name = 'employee/dept/dept_add.html'
    form_class = DeptCreateForm

    def post(self, request, *args, **kwargs):
        form = DeptCreateForm(request.POST)
        if form.is_valid():
            department = form.save()
            department.created_by = request.user
            department.save()
            # return HttpResponseRedirect(reverse_lazy('products:detail', args=[product.id]))
            messages.info(request, 'Department Added')
        # return render(request, 'employee/department/dept_list.html', {'form': form})
        return redirect('dept_list')


class DeptUpdateView(UpdateView):
    model = Department
    template_name = 'employee/dept/dept_update.html'
    form_class = DeptUpdateForm
    success_url = reverse_lazy('dept_list')


class DeptDeleteView(DeleteView):
    model = Department
    template_name = 'employee/dept/dept_delete.html'
    success_url = reverse_lazy('dept_list')


def dept_list(request):
    departments = Department.objects.order_by('id').all()
    context = {'departments': departments}
    return render(request, 'employee/dept/dept_list.html', context)


class FacultyCreateView(CreateView):
    template_name = 'employee/faculty/faculty_add.html'
    form_class = FacultyCreateForm

    def post(self, request, *args, **kwargs):
        form = FacultyCreateForm(request.POST)
        if form.is_valid():
            faculty = form.save()
            faculty.created_by = request.user
            faculty.save()
            # return HttpResponseRedirect(reverse_lazy('products:detail', args=[product.id]))
            messages.info(request, 'Faculty Added')
        # return render(request, 'employee/department/dept_list.html', {'form': form})
        return redirect('faculty_list')


class FacultyUpdateView(UpdateView):
    model = Faculty
    template_name = 'employee/faculty/faculty_update.html'
    form_class = FacultyUpdateForm
    success_url = reverse_lazy('faculty_list')


class FacultyDeleteView(DeleteView):
    model = Faculty
    template_name = 'employee/faculty/faculty_delete.html'
    success_url = reverse_lazy('faculty_list')


def faculty_list(request):
    faculties = Faculty.objects.order_by('id').all()
    context = {'faculties': faculties}
    return render(request, 'employee/faculty/faculty_list.html', context)
