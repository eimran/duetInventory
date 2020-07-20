from django.urls import path
from . import views
from .views import ProductCreateView

urlpatterns = [
    path("category-list", views.category_list, name="category_list"),
    path("category-add/", views.category_add, name='category_add'),
    path("product-list", views.product_list, name="product_list"),
    path('product-add/', views.ProductCreateView.as_view(), name='product_add'),
    path('product/edit/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('category/edit/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),
    # path('<int:pk>/', views.ProductDetailView.as_view(), name='detail')
]


