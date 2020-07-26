from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib import messages
from .filters import *
from .forms import *
from django.conf import settings
from .models import Category, Product, ProductItem, Repair, Status, Location, Property, ProductCategory


def category_add(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name', '')
        details = request.POST.get('details', '')
        parent_id = request.POST.get('parent_id', '')
        if parent_id != '':
            parent_object = Category.objects.get(id=parent_id)
        else:
            parent_object = default = None
        parent_object = Category.objects.get(id=parent_id)
        current_user = request.user

        category_obj = Category(category_name=category_name, details=details, parent_id=parent_object,
                                created_by=current_user, active_status=1)
        category_obj.save()

        categories = Category.objects.order_by('id').all()
        context = {'categories': categories}

        return render(request, 'product/category/category_list.html', context)

    else:
        context = {}
        context['form'] = CategoryCreateForm()

        return render(request, 'product/category/category_add.html', context)


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'product/category/category_update.html'
    form_class = CategoryUpdateForm
    # fields = ['category_name', 'details', 'parent_id']


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'product/category/category_delete.html'
    success_url = reverse_lazy('category_list')


def category_list(request):
    categories = Category.objects.order_by('id').all()
    context = {'categories': categories}
    return render(request, 'product/category/category_list.html', context)


class ProductCreateView(CreateView):
    template_name = 'product/product/product_add.html'
    form_class = ProductCreateForm

    def post(self, request, *args, **kwargs):
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            product.created_by = request.user
            product.save()
            messages.info(request, 'product inserted')
        return redirect('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product/product_update.html'
    form_class = ProductUpdateForm
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product/product_delete.html'
    success_url = reverse_lazy('product_list')


def product_list(request):
    products = Product.objects.order_by('id').all()
    myFilter = ProductFilter(request.GET, queryset=products)
    products = myFilter.qs
    context = {'products': products, 'myFilter': myFilter}
    return render(request, 'product/product/product_list.html', context)


# class ProductListView(ListView):
#     model = Product
#     myFilter = ProductFilter()
#     template_name = 'product/product/product_list.html'


class ProductCategoryCreateView(CreateView):
    template_name = 'product/product_category/product_category_add.html'
    form_class = ProductCategoryCreateForm

    # def get_initial(self, *args, **kwargs):
    #     initial = super(ProductCreateView, self).get_initial(**kwargs)
    #     initial['category_name'] = 'My Product'
    #     return initial

    def post(self, request, *args, **kwargs):
        form = ProductCategoryCreateForm(request.POST, request.FILES)
        if form.is_valid():
            pCat = form.save()
            pCat.created_by = request.user
            pCat.save()
            messages.info(request, 'product inserted')
        return redirect('product_category_list')


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'product/product_category/product_category_update.html'
    form_class = ProductCategoryUpdateForm
    success_url = reverse_lazy('product_category_list')


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'product/product_category/product_category_delete.html'
    success_url = reverse_lazy('product_category_list')


def product_category_list(request):
    pcats = ProductCategory.objects.order_by('id').all()
    product_category_filter = ProductCategoryFilter(request.GET, queryset=pcats)
    pcats = product_category_filter.qs
    context = {'pcats': pcats, 'product_category_filter': product_category_filter}
    return render(request, 'product/product_category/product_category_list.html', context)


class ProductItemCreateView(CreateView):
    template_name = 'product/product/product_item_add.html'
    form_class = ProductItemCreateForm

    def post(self, request, *args, **kwargs):
        form = ProductItemCreateForm(request.POST)
        if form.is_valid():
            product_item = form.save()
            product_item.created_by = request.user
            product_item.save()
            messages.info(request, 'product item inserted')
        # return render(request, 'product/product_item_list.html', {'form': form})
        return redirect('product_item_list')


class ProductItemUpdateView(UpdateView):
    model = ProductItem
    template_name = 'product/product/product_item_update.html'
    form_class = ProductItemUpdateForm
    success_url = reverse_lazy('product_item_list')


class ProductItemDeleteView(DeleteView):
    model = ProductItem
    template_name = 'product/product/product_item_delete.html'
    success_url = reverse_lazy('product_item_list')


def product_item_list(request):
    product_items = ProductItem.objects.order_by('id').all()
    product_item_filter = ProductItemFilter(request.GET, queryset=product_items)
    product_items = product_item_filter.qs
    context = {'product_items': product_items, 'product_item_filter': product_item_filter}
    return render(request, 'product/product/product_item_list.html', context)


class RepairCreateView(CreateView):
    template_name = 'product/repair/repair_add.html'
    form_class = RepairCreateForm

    # def get_initial(self, *args, **kwargs):
    #     initial = super(ProductCreateView, self).get_initial(**kwargs)
    #     initial['category_name'] = 'My Product'
    #     return initial

    def post(self, request, *args, **kwargs):
        form = RepairCreateForm(request.POST)
        if form.is_valid():
            repair = form.save()
            repair.created_by = request.user
            repair.save()
            # return HttpResponseRedirect(reverse_lazy('products:detail', args=[product.id]))
            messages.info(request, 'repair item inserted')
        # return render(request, 'product/product_list.html', {'form': form})
        return redirect('repair_list')


class RepairUpdateView(UpdateView):
    model = Repair
    template_name = 'product/repair/repair_update.html'
    form_class = RepairUpdateForm
    success_url = reverse_lazy('repair_list')


class RepairDeleteView(DeleteView):
    model = Repair
    template_name = 'product/repair/repair_delete.html'
    success_url = reverse_lazy('repair_list')


def repair_list(request):
    repairs = Repair.objects.order_by('id').all()
    context = {'repairs': repairs}
    return render(request, 'product/repair/repair_list.html', context)


class ProductStatusCreateView(CreateView):
    template_name = 'product/product/status/product_status_add.html'
    form_class = ProductStatusCreateForm

    # def get_initial(self, *args, **kwargs):
    #     initial = super(ProductCreateView, self).get_initial(**kwargs)
    #     initial['category_name'] = 'My Product'
    #     return initial

    def post(self, request, *args, **kwargs):
        form = ProductStatusCreateForm(request.POST)
        if form.is_valid():
            status = form.save()
            status.save()
            # return HttpResponseRedirect(reverse_lazy('products:detail', args=[product.id]))
            messages.info(request, 'status item inserted')
        # return render(request, 'product/product_list.html', {'form': form})
        return redirect('product_status_list')


class ProductStatusUpdateView(UpdateView):
    model = Status
    template_name = 'product/product/status/product_status_update.html'
    form_class = ProductStatusUpdateForm
    success_url = reverse_lazy('product_status_list')


class ProductStatusDeleteView(DeleteView):
    model = Status
    template_name = 'product/product/status/product_status_delete.html'
    success_url = reverse_lazy('product_status_list')


def product_status_list(request):
    statuss = Status.objects.order_by('id').all()
    context = {'statuss': statuss}
    return render(request, 'product/product/status/product_status_list.html', context)


class ProductLocationCreateView(CreateView):
    template_name = 'product/product/location/product_location_add.html'
    form_class = ProductLocationCreateForm

    # def get_initial(self, *args, **kwargs):
    #     initial = super(ProductCreateView, self).get_initial(**kwargs)
    #     initial['category_name'] = 'My Product'
    #     return initial

    def post(self, request, *args, **kwargs):
        form = ProductLocationCreateForm(request.POST)
        if form.is_valid():
            location = form.save()
            location.save()
            # return HttpResponseRedirect(reverse_lazy('products:detail', args=[product.id]))
            messages.info(request, 'Location item inserted')
        # return render(request, 'product/product_list.html', {'form': form})
        return redirect('product_location_list')


class ProductLocationUpdateView(UpdateView):
    model = Location
    template_name = 'product/product/location/product_location_update.html'
    form_class = ProductLocationUpdateForm
    success_url = reverse_lazy('product_location_list')


class ProductLocationDeleteView(DeleteView):
    model = Location
    template_name = 'product/product/location/product_location_delete.html'
    success_url = reverse_lazy('product_location_list')


def product_location_list(request):
    locations = Location.objects.order_by('id').all()
    context = {'locations': locations}
    return render(request, 'product/product/location/product_location_list.html', context)


class ProductPropertyCreateView(CreateView):
    template_name = 'product/product/property/product_property_add.html'
    form_class = ProductPropertyCreateForm

    # def get_initial(self, *args, **kwargs):
    #     initial = super(ProductCreateView, self).get_initial(**kwargs)
    #     initial['category_name'] = 'My Product'
    #     return initial

    def post(self, request, *args, **kwargs):
        form = ProductPropertyCreateForm(request.POST)
        if form.is_valid():
            property = form.save()
            property.created_by = request.user
            property.save()
            messages.info(request, 'Product Property Inserted')
        # return render(request, 'product/product_list.html', {'form': form})
        return redirect('product_property_list')


class ProductPropertyUpdateView(UpdateView):
    model = Property
    template_name = 'product/product/location/product_location_update.html'
    form_class = ProductPropertyUpdateForm
    success_url = reverse_lazy('product_property_list')


class ProductPropertyDeleteView(DeleteView):
    model = Property
    template_name = 'product/product/property/product_property_delete.html'
    success_url = reverse_lazy('product_property_list')


def product_property_list(request):
    properties = Property.objects.order_by('id').all()
    context = {'properties': properties}
    return render(request, 'product/product/property/product_property_list.html', context)
