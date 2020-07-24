from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.contrib import messages
from django.conf import settings
from .models import Category, Product, Repair
from .forms import CategoryCreateForm, CategoryUpdateForm, ProductCreateForm, ProductUpdateForm, RepairCreateForm, RepairUpdateForm


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
    #fields = ['category_name', 'details', 'parent_id']


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

    # def get_initial(self, *args, **kwargs):
    #     initial = super(ProductCreateView, self).get_initial(**kwargs)
    #     initial['category_name'] = 'My Product'
    #     return initial

    def post(self, request, *args, **kwargs):
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.created_by = request.user
            product.save()
            # return HttpResponseRedirect(reverse_lazy('products:detail', args=[product.id]))
            messages.info(request, 'product inserted')
        # return render(request, 'product/product_list.html', {'form': form})
        return redirect('product_list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/product/product_update.html'
    form_class = ProductUpdateForm
    #fields = ['p_name', 'country_of_origin', 'brand', 'p_details']


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product/product_delete.html'
    success_url = reverse_lazy('product_list')


def product_list(request):
    products = Product.objects.order_by('id').all()
    context = {'products': products}
    return render(request, 'product/product/product_list.html', context)


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
    #fields = ['p_name', 'country_of_origin', 'brand', 'p_details']


class RepairDeleteView(DeleteView):
    model = Repair
    template_name = 'product/repair/repair_delete.html'
    success_url = reverse_lazy('repair_list')


def repair_list(request):
    repairs = Repair.objects.order_by('id').all()
    context = {'repairs': repairs}
    return render(request, 'product/repair/repair_list.html', context)
