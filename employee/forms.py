from django import forms
from .models import Employee, Department, Faculty, WorkRecord


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'cell_no', 'email', 'address', 'gender', 'dob', 'employee_no',
                  'joining_date', 'category', 'image')

    #     widgets = {
    #         'p_name': forms.TextInput(attrs={'class': 'form-control'}),
    #         'country_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
    #         'brand': forms.TextInput(attrs={'class': 'form-control'}),
    #         'p_details': forms.TextInput(attrs={'class': 'form-control'}),
    #     }
    #
    # def __init__(self, *args, **kwargs):
    #     super(EmployeeCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['p_name'].label = "Product Name"
    #     self.fields['country_of_origin'].label = "Country of Origin"
    #     self.fields['brand'].label = "Brand"
    #     self.fields['p_details'].label = "Details"


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'cell_no', 'email', 'address', 'gender', 'dob', 'employee_no',
                  'joining_date', 'category', 'image')

        # widgets = {
        #     'p_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'country_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
        #     'brand': forms.TextInput(attrs={'class': 'form-control'}),
        #     'p_details': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    # def __init__(self, *args, **kwargs):
    #     super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
    #     self.fields['p_name'].label = "Product Name"


class DeptCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'code', 'acronym', 'description', 'type', 'faculty')


class DeptUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'code', 'acronym', 'description', 'type', 'faculty')


class FacultyCreateForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('name', 'code', 'acronym', 'description', 'type')


class FacultyUpdateForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('name', 'code', 'acronym', 'description', 'type')


class WorkRecordCreateForm(forms.ModelForm):
    class Meta:
        model = WorkRecord
        fields = ('employee', 'designation', 'role_name', 'from_date', 'to_date', 'is_additional', 'description')


class WorkRecordUpdateForm(forms.ModelForm):
    class Meta:
        model = WorkRecord
        fields = ('employee', 'designation', 'role_name', 'from_date', 'to_date', 'is_additional', 'description')
