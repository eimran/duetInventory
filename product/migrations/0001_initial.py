# Generated by Django 3.0.8 on 2020-07-26 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='Category Name')),
                ('details', models.CharField(max_length=500, verbose_name='Category Details')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('active_status', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_modified_by', to=settings.AUTH_USER_MODEL)),
                ('parent_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=100)),
                ('country_of_origin', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('p_details', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_item_name', models.CharField(max_length=100)),
                ('qr_code_key', models.CharField(max_length=5000)),
                ('actual_cost', models.FloatField()),
                ('depreciation', models.FloatField()),
                ('purchase_date', models.DateField(verbose_name='Purchase Date')),
                ('expiry_date', models.DateField(verbose_name='Expiry Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_item_created_by', to=settings.AUTH_USER_MODEL)),
                ('dept_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.Department', verbose_name='Department')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_item_modified_by', to=settings.AUTH_USER_MODEL)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Location', verbose_name='Location')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product')),
                ('responsible_employee_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.Employee', verbose_name='Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(max_length=500)),
                ('repair_request_date', models.DateField(verbose_name='Repair Request Date')),
                ('estimated_delivery_date', models.DateField(verbose_name='Estimated Delivery Date')),
                ('actual_delivery_date', models.DateField(verbose_name='Actual Delivery Date')),
                ('estimated_cost', models.FloatField()),
                ('actual_cost', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='repair_request_approved_by', to='employee.Employee', verbose_name='Approved by')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repair_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repair_modified_by', to=settings.AUTH_USER_MODEL)),
                ('product_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.ProductItem', verbose_name='Product Item')),
                ('responsible_employee_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='responsible_employee_id', to='employee.Employee', verbose_name='Responsible Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=100)),
                ('property_value', models.CharField(max_length=100)),
                ('property_details', models.CharField(max_length=500)),
                ('priority', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='property_modified_by', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product')),
            ],
        ),
        migrations.AddField(
            model_name='productitem',
            name='status_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Status', verbose_name='Status'),
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Category', verbose_name='Category')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_category_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_category_modified_by', to=settings.AUTH_USER_MODEL)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalLoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField(verbose_name='Loan Date')),
                ('loan_payoff_date', models.DateField(verbose_name='Loan Pay-off Date Date')),
                ('details', models.CharField(max_length=5000)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified At')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personal_loan_created_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personal_loan_modified_by', to=settings.AUTH_USER_MODEL)),
                ('loan_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loan_given_by', to='employee.Employee', verbose_name='Loan Given by')),
                ('loan_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.ProductItem', verbose_name='Loan Item')),
                ('loan_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='loan_given_to', to='employee.Employee', verbose_name='Loan Given to')),
            ],
        ),
    ]
