import django_filters
from .models import *


class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ('p_name', 'country_of_origin', 'brand', 'p_details')


class ProductItemFilter(django_filters.FilterSet):
    class Meta:
        model = ProductItem
        fields = ('p_item_name', 'qr_code_key', 'purchase_date', 'expiry_date',
                  'responsible_employee_id', 'dept_id', 'location_id', 'status_id')


class ProductCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = ProductCategory
        fields = ('product_id', 'category_id')

