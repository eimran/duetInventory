from django import forms
from .models import Employee, Department, Faculty, WorkRecord, Designation


class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'cell_no', 'email', 'address', 'gender', 'dob', 'employee_no',
                  'joining_date', 'category', 'image')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cell_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': DateInput(attrs={'class': 'form-control'}),
            'employee_no': forms.TextInput(attrs={'class': 'form-control'}),
            'joining_date': DateInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeCreateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['cell_no'].label = "Cell No"
        self.fields['email'].label = "Email"
        self.fields['address'].label = "Address"
        self.fields['email'].label = "Email"
        self.fields['dob'].label = "Date of Birth"
        self.fields['employee_no'].label = "Employee No"


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'cell_no', 'email', 'address', 'gender', 'dob', 'employee_no',
                  'joining_date', 'category', 'image')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cell_no': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': DateInput(attrs={'class': 'form-control'}),
            'employee_no': forms.TextInput(attrs={'class': 'form-control'}),
            'joining_date': DateInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['cell_no'].label = "Cell No"
        self.fields['email'].label = "Email"
        self.fields['address'].label = "Address"
        self.fields['email'].label = "Email"
        self.fields['dob'].label = "Date of Birth"
        self.fields['employee_no'].label = "Employee No"


class DeptCreateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'code', 'acronym', 'description', 'type', 'faculty')

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'code': forms.TextInput(attrs={'class': 'form-control'}),
                'acronym': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'type': forms.Select(attrs={'class': 'form-control'}),
                'faculty': forms.Select(attrs={'class': 'form-control'}),

            }

    def __init__(self, *args, **kwargs):
        super(DeptCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Department Name"
        self.fields['code'].label = "Code"


class DeptUpdateForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name', 'code', 'acronym', 'description', 'type', 'faculty')

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'code': forms.TextInput(attrs={'class': 'form-control'}),
                'acronym': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'type': forms.Select(attrs={'class': 'form-control'}),
                'faculty': forms.Select(attrs={'class': 'form-control'}),

            }

    def __init__(self, *args, **kwargs):
        super(DeptUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Department Name"
        self.fields['code'].label = "Code"


class FacultyCreateForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('name', 'code', 'acronym', 'description', 'type')

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'code': forms.TextInput(attrs={'class': 'form-control'}),
                'acronym': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'type': forms.Select(attrs={'class': 'form-control'}),
            }

    def __init__(self, *args, **kwargs):
        super(FacultyCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Faculty Name"
        self.fields['code'].label = "Code"


class FacultyUpdateForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ('name', 'code', 'acronym', 'description', 'type')

        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'code': forms.TextInput(attrs={'class': 'form-control'}),
                'acronym': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'type': forms.Select(attrs={'class': 'form-control'}),
            }

    def __init__(self, *args, **kwargs):
        super(FacultyUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Faculty Name"
        self.fields['code'].label = "Code"


class WorkRecordCreateForm(forms.ModelForm):
    class Meta:
        model = WorkRecord
        fields = ('employee', 'designation', 'role_name', 'from_date', 'to_date', 'is_additional', 'description')

        widgets = {
                'employee': forms.Select(attrs={'class': 'form-control'}),
                'designation': forms.Select(attrs={'class': 'form-control'}),
                'role_name': forms.TextInput(attrs={'class': 'form-control'}),
                'from_date': DateInput(attrs={'class': 'form-control'}),
                'to_date': DateInput(attrs={'class': 'form-control'}),
                'is_additional': forms.CheckboxInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(WorkRecordCreateForm, self).__init__(*args, **kwargs)
        self.fields['from_date'].label = "Assign Date"
        self.fields['to_date'].label = "Release Date"


class WorkRecordUpdateForm(forms.ModelForm):
    class Meta:
        model = WorkRecord
        fields = ('employee', 'designation', 'role_name', 'from_date', 'to_date', 'is_additional', 'description')
        widgets = {
                'employee': forms.Select(attrs={'class': 'form-control'}),
                'designation': forms.Select(attrs={'class': 'form-control'}),
                'role_name': forms.TextInput(attrs={'class': 'form-control'}),
                'from_date': DateInput(attrs={'class': 'form-control'}),
                'to_date': DateInput(attrs={'class': 'form-control'}),
                'is_additional': forms.CheckboxInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(WorkRecordUpdateForm, self).__init__(*args, **kwargs)
        self.fields['from_date'].label = "Assign Date"
        self.fields['to_date'].label = "Release Date"


class DesignationCreateForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ('name', 'description')
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(DesignationCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Designation"


class DesignationUpdateForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ('name', 'description')

        fields = ('name', 'description')
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(DesignationUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Designation"
