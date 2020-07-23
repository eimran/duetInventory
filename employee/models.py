from django.db import models
from django.conf import settings
from employee.choices import DEPARTMENT_TYPE, GENDER, EMPLOYEE_CATEGORY


class Designation(models.Model):
    name = models.CharField(max_length=200, verbose_name = 'Name')
    description = models.TextField(null=True, blank = True, verbose_name = 'Description')

    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='designation_created_by')

    last_modified_at = models.DateTimeField(auto_now = True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='designation_modified_by')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Faculty(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    code = models.CharField(max_length=10, verbose_name='Code', null=True)
    acronym = models.CharField(max_length=10, null=True, verbose_name='Acronym')
    description = models.TextField(null=True, blank=True, verbose_name='Description')
    type = models.CharField(max_length=2, choices=DEPARTMENT_TYPE, verbose_name='Type')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='faculty_created_by')

    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='faculty_modified_by')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Department(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name')
    code = models.CharField(max_length=10, verbose_name='Code', null=True)
    acronym = models.CharField(max_length = 10, null = True, verbose_name = 'Acronym')
    description = models.TextField(null=True, blank = True, verbose_name='Description')
    type = models.CharField(max_length=2, choices=DEPARTMENT_TYPE, verbose_name = 'Type')
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='department_created_by')

    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='department_modified_by')

    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Employee(models.Model):
    # employee_id = models.AutoField
    first_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='Last Name')

    cell_no = models.CharField(verbose_name='Cell no', max_length=20, null=True, blank=True)
    email = models.CharField(verbose_name='Email', max_length=50, null=True, blank=True)
    address = models.TextField(blank=True, null=True, verbose_name='Address')

    gender = models.CharField(max_length=1, choices=GENDER, default='m', verbose_name="Gender")
    dob = models.DateField(verbose_name='Date of Birth')
    image = models.FileField(upload_to='photos', null=True, blank=True)

    employee_no = models.CharField(verbose_name='Employee no', max_length=20, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Created At")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='employee_created_by')

    last_modified_at = models.DateTimeField(auto_now=True, verbose_name="Last Modified At")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                                         related_name='employee_modified_by')

    active_status = models.IntegerField(default=1)

    joining_date = models.DateField(null=True, verbose_name="Joining Date")
    category = models.CharField(max_length=1, choices=EMPLOYEE_CATEGORY, verbose_name='Category', default='t')

    designation = models.ForeignKey(Designation, verbose_name='Designation', on_delete=models.PROTECT, null=True)
    department = models.ForeignKey(Department, verbose_name='Department', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + self.employee_no + ")"


class DeptWiseHead(models.Model):
    # employee_id = models.AutoField
    head_id = models.ForeignKey(Employee, verbose_name='Employee', on_delete=models.PROTECT)
    dept_id = models.ForeignKey(Department, verbose_name='Department', on_delete=models.PROTECT)


class FacultyWiseDean(models.Model):
    # employee_id = models.AutoField
    faculty_id = models.ForeignKey(Faculty, verbose_name='Department', on_delete=models.PROTECT)
    dean_id = models.ForeignKey(Employee, verbose_name='Employee', on_delete=models.PROTECT)