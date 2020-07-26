from django.db import models
from django.urls import reverse
from django.conf import settings

from employee.models import Employee, Department


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Category Name')
    details = models.CharField(max_length=500, verbose_name='Category Details')

    parent_id = models.ForeignKey('self', null=True, related_name='category', on_delete=models.CASCADE, unique=False)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='category_created_by')

    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='category_modified_by')

    active_status = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('category_list')

    def __str__(self):
        return self.category_name


class Product(models.Model):
    p_name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    p_details = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='product_created_by')

    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='product_modified_by')

    def get_absolute_url(self):
        return reverse('product_list')

    def __str__(self):
        return self.p_name


class ProductCategory(models.Model):
    product_id = models.ForeignKey(Product, verbose_name='Product', on_delete=models.PROTECT)
    category_id = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='product_category_created_by')

    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='product_category_modified_by')

    def __str__(self):
        return self.product_id.p_name + "(" + self.category_id.category_name + ")"


class Property(models.Model):
    property_name = models.CharField(max_length=100)
    property_value = models.CharField(max_length=100)
    property_details = models.CharField(max_length=500)
    priority = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='property_created_by')

    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='property_modified_by')

    product_id = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.property_name


class Location(models.Model):
    location_name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

    def __str__(self):
        return self.location_name


class Status(models.Model):
    status_name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

    def __str__(self):
        return self.status_name


class ProductItem(models.Model):
    p_item_name = models.CharField(max_length=100)

    qr_code_key = models.CharField(max_length=5000)
    actual_cost = models.FloatField()
    depreciation = models.FloatField()
    purchase_date = models.DateField(verbose_name='Purchase Date')
    expiry_date = models.DateField(verbose_name='Expiry Date')

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='product_item_created_by')

    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='product_item_modified_by')

    responsible_employee_id = models.ForeignKey(Employee, verbose_name='Employee', on_delete=models.PROTECT)
    dept_id = models.ForeignKey(Department, verbose_name='Department', on_delete=models.PROTECT)

    product_id = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)

    location_id = models.ForeignKey(Location, verbose_name='Location', on_delete=models.PROTECT)
    status_id = models.ForeignKey(Status, verbose_name='Status', on_delete=models.PROTECT)

    def __str__(self):
        return self.p_item_name


class Repair(models.Model):
    details = models.CharField(max_length=500)
    repair_request_date = models.DateField(verbose_name='Repair Request Date')
    estimated_delivery_date = models.DateField(verbose_name='Estimated Delivery Date')
    actual_delivery_date = models.DateField(verbose_name='Actual Delivery Date')

    estimated_cost = models.FloatField()
    actual_cost = models.FloatField()

    approved_by = models.ForeignKey(Employee, verbose_name='Approved by', on_delete=models.PROTECT,
                                    related_name='repair_request_approved_by')
    responsible_employee_id = models.ForeignKey(Employee, verbose_name='Responsible Employee', on_delete=models.PROTECT,
                                                related_name='responsible_employee_id')
    product_item_id = models.ForeignKey(ProductItem, verbose_name='Product Item', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='repair_created_by')

    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='repair_modified_by')

    def __str__(self):
        return self.product_item_id.p_item_name + "(" + self.approved_by.dept_id + ")"


class PersonalLoan(models.Model):
    loan_date = models.DateField(verbose_name='Loan Date')
    loan_payoff_date = models.DateField(verbose_name='Loan Pay-off Date Date')
    details = models.CharField(max_length=5000)
    loan_from = models.ForeignKey(Employee, verbose_name='Loan Given by', on_delete=models.PROTECT,
                                  related_name='loan_given_by')
    loan_to = models.ForeignKey(Employee, verbose_name='Loan Given to', on_delete=models.PROTECT,
                                related_name='loan_given_to')
    loan_item = models.ForeignKey(ProductItem, verbose_name='Loan Item', on_delete=models.PROTECT)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='personal_loan_created_by')
    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='personal_loan_modified_by')

    def __str__(self):
        return self.loan_item.p_item_name + "(" + self.loan_from.first_name + "-> )" + self.loan_to.first_name + ")"
