from django.db import models
# from autoslug import AutoSlugField
from django.conf import settings
from employee.choices import DEPARTMENT_TYPE, GENDER


# Create your models here.
class Employee(models.Model):
    # employee_id = models.AutoField
    first_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Last Name')

    cell_no = models.CharField(verbose_name='Cell no', max_length=20, null=True, blank=True)
    email = models.CharField(verbose_name='Email', max_length=50, null=True, blank=True)
    address = models.TextField(blank=True, null=True, verbose_name='Address')

    # GENDER_MALE = 0
    # GENDER_FEMALE = 1
    # GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    # gender = models.IntegerField(choices=GENDER_CHOICES)
    # dob = models.DateField(max_length=8)

    gender = models.CharField(max_length=1, choices=GENDER, default='m', verbose_name="Gender")
    dob = models.DateField(verbose_name='Date of Birth')
    image = models.FileField(upload_to='photos', null=True, blank=True)

    employee_no = models.CharField(verbose_name='Employee no', max_length=20, null=True, blank=True)

    # created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    # created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
    #                                related_name='employee_created_by')
    #
    # last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")
    # last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
    #                                      related_name='employee_modified_by')
    #
    # # slug = AutoSlugField(populate_from='first_name', unique=True, null=True, always_update=True, default=None)
    # active_status = models.IntegerField(default=1)

    # department = models.ForeignKey(Department, verbose_name='Department', on_delete=models.PROTECT)
    # slug = AutoSlugField(populate_from='first_name', unique=True, always_update=True, default=None)
    # joining_date = models.DateField(null=True, verbose_name="Joining Date")
    # designation = models.ForeignKey(Designation, verbose_name='Designation', on_delete=models.PROTECT)
    # grade = models.ForeignKey('duet_account.Grade', null=True, verbose_name='Grade', on_delete=models.PROTECT)
    # category = models.CharField(max_length= 1, choices= EMPLOYEE_CATEGORY, verbose_name='Category', default = 't')

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + self.employee_no + ")"
