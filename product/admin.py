from django.contrib import admin
from .models import Category
from product.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Property)
admin.site.register(Location)
admin.site.register(Status)
admin.site.register(ProductItem)
admin.site.register(Repair)



