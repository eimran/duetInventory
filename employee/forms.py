from django import forms
from .models import Employee


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'cell_no', 'email', 'address', 'gender', 'dob', 'joining_date')
        #
        # widgets = {
        #     'p_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'country_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
        #     'brand': forms.TextInput(attrs={'class': 'form-control'}),
        #     'p_details': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    # def __init__(self, *args, **kwargs):
    #     super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
    #     self.fields['p_name'].label = "Product Name"
