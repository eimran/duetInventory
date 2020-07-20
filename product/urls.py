from django.urls import path
from . import views
from .views import ProductCreateView

urlpatterns = [
    path("category-list", views.category_list, name="category_list"),
    path("category-add/", views.category_add, name='category_add'),
    path("product-list", views.product_list, name="product_list"),
    path('product-add/', views.ProductCreateView.as_view(), name='product_add'),
    # path('<int:pk>/', views.ProductDetailView.as_view(), name='detail')
]
