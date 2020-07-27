from django import forms
from .models import *

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
        fields = ('p_name', 'country_of_origin', 'brand', 'p_details', 'image')

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
        self.fields['image'].label = "Upload Image"


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('p_name', 'country_of_origin', 'brand', 'p_details', 'last_modified_by', 'image')

        widgets = {
            'p_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'p_details': forms.TextInput(attrs={'class': 'form-control'}),
            'last_modified_by': forms.HiddenInput(),

        }

    def __init__(self, *args, **kwargs):
        super(ProductUpdateForm, self).__init__(*args, **kwargs)
        self.fields['p_name'].label = "Product Name"
        self.fields['country_of_origin'].label = "Country of Origin"
        self.fields['brand'].label = "Brand"
        self.fields['p_details'].label = "Details"
        self.fields['last_modified_by'].value = "1"
        self.fields['image'].value = "Update Image"


class ProductCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('product_id', 'category_id')

        widgets = {
            'product_id': forms.Select(attrs={'class': 'form-control'}),
            'category_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductCategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['product_id'].label = "Product Name"
        self.fields['category_id'].label = "Category Name"


class ProductCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('product_id', 'category_id')

        widgets = {
            'product_id': forms.Select(attrs={'class': 'form-control'}),
            'category_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductCategoryUpdateForm, self).__init__(*args, **kwargs)
        self.fields['product_id'].label = "Product Name"
        self.fields['category_id'].label = "Category Name"


class ProductItemCreateForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = ('p_item_name', 'qr_code_key', 'actual_cost', 'depreciation', 'purchase_date', 'expiry_date',
                  'responsible_employee_id', 'dept_id', 'product_id', 'location_id', 'status_id')

        widgets = {
            'p_item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'qr_code_key': forms.TextInput(attrs={'class': 'form-control'}),
            'actual_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'depreciation': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'expiry_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'responsible_employee_id': forms.Select(attrs={'class': 'form-control'}),
            'dept_id': forms.Select(attrs={'class': 'form-control'}),
            'product_id': forms.Select(attrs={'class': 'form-control'}),
            'location_id': forms.Select(attrs={'class': 'form-control'}),
            'status_id': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(ProductItemCreateForm, self).__init__(*args, **kwargs)
        self.fields['p_item_name'].label = "Product Item Name"
        self.fields['qr_code_key'].label = "QR Code"
        self.fields['actual_cost'].label = "Actual Cost"
        self.fields['depreciation'].label = "Depreciation"
        self.fields['purchase_date'].label = "Purchase Date"
        self.fields['expiry_date'].label = "Expiry Date"
        self.fields['responsible_employee_id'].label = "Responsible Employee ID"
        self.fields['dept_id'].label = "Department"
        self.fields['product_id'].label = "Product"
        self.fields['location_id'].label = "Location"
        self.fields['status_id'].label = "Status"


class ProductItemUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = ('p_item_name', 'qr_code_key', 'actual_cost', 'depreciation', 'purchase_date', 'expiry_date',
                  'responsible_employee_id', 'dept_id', 'product_id', 'location_id', 'status_id')

        widgets = {
            'p_item_name': forms.TextInput(attrs={'class': 'form-control'}),
            'qr_code_key': forms.TextInput(attrs={'class': 'form-control'}),
            'actual_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'depreciation': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'expiry_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'responsible_employee_id': forms.Select(attrs={'class': 'form-control'}),
            'dept_id': forms.Select(attrs={'class': 'form-control'}),
            'product_id': forms.Select(attrs={'class': 'form-control'}),
            'location_id': forms.Select(attrs={'class': 'form-control'}),
            'status_id': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(ProductItemUpdateForm, self).__init__(*args, **kwargs)
        self.fields['p_item_name'].label = "Product Item Name"
        self.fields['qr_code_key'].label = "QR Code"
        self.fields['actual_cost'].label = "Actual Cost"
        self.fields['depreciation'].label = "Depreciation"
        self.fields['purchase_date'].label = "Purchase Date"
        self.fields['expiry_date'].label = "Expiry Date"
        self.fields['responsible_employee_id'].label = "Responsible Employee ID"
        self.fields['dept_id'].label = "Department"
        self.fields['product_id'].label = "Product"
        self.fields['location_id'].label = "Location"
        self.fields['status_id'].label = "Status"


class ProductStatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('status_name', 'details')

        widgets = {
            'status_name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductStatusCreateForm, self).__init__(*args, **kwargs)
        self.fields['status_name'].label = "Product Status Name"
        self.fields['details'].label = "Details"


class ProductStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ('status_name', 'details')
        widgets = {
            'status_name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductStatusUpdateForm, self).__init__(*args, **kwargs)
        self.fields['status_name'].label = "Product Status Name"
        self.fields['details'].label = "Details"


class ProductLocationCreateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('location_name', 'details')
        widgets = {
            'location_name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductLocationCreateForm, self).__init__(*args, **kwargs)
        self.fields['location_name'].label = "Product Location Name"
        self.fields['details'].label = "Details"


class ProductLocationUpdateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('location_name', 'details')
        widgets = {
            'location_name': forms.TextInput(attrs={'class': 'form-control'}),
            'details': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductLocationUpdateForm, self).__init__(*args, **kwargs)
        self.fields['location_name'].label = "Product Location Name"
        self.fields['details'].label = "Details"


class RepairCreateForm(forms.ModelForm):
    class Meta:
        model = Repair

        fields = ('details', 'repair_request_date', 'estimated_delivery_date', 'actual_delivery_date', 'estimated_cost',
                  'actual_cost', 'approved_by', 'responsible_employee_id', 'product_item_id')

        widgets = {
            'details': forms.TextInput(attrs={'class': 'form-control'}),
            'repair_request_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'estimated_delivery_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'actual_delivery_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'estimated_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'actual_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'approved_by': forms.Select(attrs={'class': 'form-control'}),
            'responsible_employee_id': forms.Select(attrs={'class': 'form-control'}),
            'product_item_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(RepairCreateForm, self).__init__(*args, **kwargs)
        self.fields['details'].label = "Product Details"
        self.fields['repair_request_date'].label = "Request Date"
        self.fields['estimated_delivery_date'].label = "Estimated Delivery Date"
        self.fields['actual_delivery_date'].label = "Actual Delivery Date"
        self.fields['estimated_cost'].label = "Estimated Cost"
        self.fields['actual_cost'].label = "Actual Cost"
        self.fields['approved_by'].label = "Approved By"
        self.fields['responsible_employee_id'].label = "Responsible Person"
        self.fields['product_item_id'].label = "Product Item Name"


class RepairUpdateForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('details', 'repair_request_date', 'estimated_delivery_date', 'actual_delivery_date', 'estimated_cost',
                  'actual_cost', 'approved_by', 'responsible_employee_id', 'product_item_id')

        widgets = {
            'details': forms.TextInput(attrs={'class': 'form-control'}),
            'repair_request_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'estimated_delivery_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'actual_delivery_date': forms.DateInput(attrs={'class': 'datepicker form-control'}),
            'estimated_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'actual_cost': forms.TextInput(attrs={'class': 'form-control'}),
            'approved_by': forms.Select(attrs={'class': 'form-control'}),
            'responsible_employee_id': forms.Select(attrs={'class': 'form-control'}),
            'product_item_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(RepairUpdateForm, self).__init__(*args, **kwargs)
        self.fields['details'].label = "Product Details"
        self.fields['repair_request_date'].label = "Request Date"
        self.fields['estimated_delivery_date'].label = "Estimated Delivery Date"
        self.fields['actual_delivery_date'].label = "Actual Delivery Date"
        self.fields['estimated_cost'].label = "Estimated Cost"
        self.fields['actual_cost'].label = "Actual Cost"
        self.fields['approved_by'].label = "Approved By"
        self.fields['responsible_employee_id'].label = "Responsible Person"
        self.fields['product_item_id'].label = "Product Item Name"


class ProductPropertyCreateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('property_name', 'property_value', 'property_details', 'priority', 'product_id')

        widgets = {
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
            'property_value': forms.TextInput(attrs={'class': 'form-control'}),
            'property_details': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
            'product_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductPropertyCreateForm, self).__init__(*args, **kwargs)
        self.fields['property_name'].label = "Property Name"
        self.fields['property_value'].label = "Property Value"
        self.fields['property_details'].label = "Property Details"
        self.fields['priority'].label = "Priority"
        self.fields['product_id'].label = "Product"


class ProductPropertyUpdateForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ('property_name', 'property_value', 'property_details', 'priority', 'product_id')

        widgets = {
            'property_name': forms.TextInput(attrs={'class': 'form-control'}),
            'property_value': forms.TextInput(attrs={'class': 'form-control'}),
            'property_details': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.TextInput(attrs={'class': 'form-control'}),
            'product_id': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(ProductPropertyUpdateForm, self).__init__(*args, **kwargs)
        self.fields['property_name'].label = "Property Name"
        self.fields['property_value'].label = "Property Value"
        self.fields['property_details'].label = "Property Details"
        self.fields['priority'].label = "Priority"
        self.fields['product_id'].label = "Product"
