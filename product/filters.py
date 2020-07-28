import django_filters
from .models import *


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ('p_name', 'country_of_origin', 'brand', 'p_details')


class ProductPropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ('property_name', 'property_value', 'property_details', 'product_id')


class ProductItemFilter(django_filters.FilterSet):
    class Meta:
        model = ProductItem
        fields = ('p_item_name', 'qr_code_key', 'product_id', 'purchase_date', 'expiry_date',
                  'responsible_employee_id', 'dept_id', 'location_id', 'status_id')

    def __init__(self, *args, **kwargs):
        super(ProductItemFilter, self).__init__(*args, **kwargs)
        self.filters['p_item_name'].label = "Item Name"
        # self.filters['p_item_name'].extra.update(
        #     {'p_item_name': 'Item Name'})


class ProductRepairFilter(django_filters.FilterSet):
    class Meta:
        model = Repair
        fields = ('product_item_id', 'details', 'repair_request_date', 'actual_delivery_date', 'responsible_employee_id')


class ProductCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = ProductCategory
        fields = ('product_id', 'category_id')


class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = ('category_name', 'details', 'parent_id')




