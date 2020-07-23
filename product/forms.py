from django import forms
from .models import Category, Product


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'details', 'parent_id')

        widgets = {
            'category_name': forms.TextInput(
                attrs={'class': 'form-control form-control-user'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_id': forms.Select(attrs={'class': 'form-control'}),
        }
        # fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].label = "Category Name"
        self.fields['details'].label = "Details"
        self.fields['parent_id'].label = "Parent ID"


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', 'details', 'parent_id')

        widgets = {
            'category_name': forms.TextInput(
                attrs={'class': 'form-control form-control-user'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_id': forms.Select(attrs={'class': 'form-control'}),
        }
        # fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CategoryUpdateForm, self).__init__(*args, **kwargs)
        self.fields['category_name'].label = "Category Name"
        self.fields['details'].label = "Details"
        self.fields['parent_id'].label = "Parent ID"


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('p_name', 'country_of_origin', 'brand', 'p_details')

        widgets = {
            'p_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'p_details': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['p_name'].label = "Product Name"
        self.fields['country_of_origin'].label = "Country of Origin"
        self.fields['brand'].label = "Brand"
        self.fields['p_details'].label = "Details"


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('p_name', 'country_of_origin', 'brand', 'p_details', 'last_modified_by')

        widgets = {
            'p_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'p_details': forms.TextInput(attrs={'class': 'form-control'}),
            'last_modified_by': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(ProductUpdateForm, self).__init__(*args, **kwargs)
        self.fields['p_name'].label = "Product Name"
        self.fields['country_of_origin'].label = "Country of Origin"
        self.fields['brand'].label = "Brand"
        self.fields['p_details'].label = "Details"
        self.fields['last_modified_by'].value = "1"
