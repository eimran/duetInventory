from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Employee
from .forms import EmployeeUpdateForm, EmployeeCreateForm
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
    #fields = ['category_name', 'details', 'parent_id']