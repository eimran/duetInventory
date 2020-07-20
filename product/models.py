from django.db import models
from django.urls import reverse
from django.conf import settings


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Category Name')
    details = models.CharField(max_length=500, verbose_name='Category Details')

    parent_id = models.ForeignKey('self', null=True, related_name='category', on_delete=models.CASCADE, unique=False)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    # last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")
    # last_modified_by = models.ForeignKey(settings.auth_user, null=True, blank=True, on_delete=models.SET_NULL)
    #
    active_status = models.IntegerField(default=0)

    # def __str__(self):
    #     return "<Category: {} {}>".format(self.category_name)

    def __repr__(self):
        return self.id
        # return self.parent_id.category_name


class Product(models.Model):
    p_name = models.CharField(max_length=100)
    country_of_origin = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    p_details = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    # def get_absolute_url(self):
    #     return reverse('products:detail', args=[self.id])

    def __str__(self):
        return self.p_name

