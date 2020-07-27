from django.urls import path
from . import views
from .views import ProductCreateView

urlpatterns = [
    path("category-list", views.category_list, name="category_list"),
    path("category-add/", views.category_add, name='category_add'),
    path("product-list", views.product_list, name="product_list"),
    # path("product-list", views.ProductListView.as_view(), name="product_list"),
    path('product-add/', views.ProductCreateView.as_view(), name='product_add'),
    path('product-add/<category_id>', views.product_add, name='product_add2'),
    path('product/edit/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('category/edit/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>', views.CategoryDeleteView.as_view(), name='category_delete'),

    path('repair-add/', views.RepairCreateView.as_view(), name='repair_add'),
    path("repair-list", views.repair_list, name="repair_list"),
    path('repair/edit/<int:pk>', views.RepairUpdateView.as_view(), name='repair_update'),
    path('repair/delete/<int:pk>', views.RepairDeleteView.as_view(), name='repair_delete'),
    # path('<int:pk>/', views.ProductDetailView.as_view(), name='detail')

    path('product-item-add/', views.ProductItemCreateView.as_view(), name='product_item_add'),
    path("product-item-list", views.product_item_list, name="product_item_list"),
    path('product-item/edit/<int:pk>', views.ProductItemUpdateView.as_view(), name='product_item_update'),
    path('product-item/delete/<int:pk>', views.ProductItemDeleteView.as_view(), name='product_item_delete'),

    path('product-status-add/', views.ProductStatusCreateView.as_view(), name='product_status_add'),
    path("product-status-list", views.product_status_list, name="product_status_list"),
    path('product-status/edit/<int:pk>', views.ProductStatusUpdateView.as_view(), name='product_status_update'),
    path('product-status/delete/<int:pk>', views.ProductStatusDeleteView.as_view(), name='product_status_delete'),

    path('product-location-add/', views.ProductLocationCreateView.as_view(), name='product_location_add'),
    path("product-location-list", views.product_location_list, name="product_location_list"),
    path('product-location/edit/<int:pk>', views.ProductLocationUpdateView.as_view(), name='product_location_update'),
    path('product-location/delete/<int:pk>', views.ProductLocationDeleteView.as_view(), name='product_location_delete'),

    path('product-property-add/', views.ProductPropertyCreateView.as_view(), name='product_property_add'),
    path("product-property-list", views.product_property_list, name="product_property_list"),
    path('product-property/edit/<int:pk>', views.ProductPropertyUpdateView.as_view(), name='product_property_update'),
    path('product-property/delete/<int:pk>', views.ProductPropertyDeleteView.as_view(), name='product_property_delete'),

    path('product-category-add/', views.ProductCategoryCreateView.as_view(), name='product_category_add'),
    path("product-category-list", views.product_category_list, name="product_category_list"),
    path('product-category/edit/<int:pk>', views.ProductCategoryUpdateView.as_view(), name='product_category_update'),
    path('product-category/delete/<int:pk>', views.ProductCategoryDeleteView.as_view(), name='product_category_delete'),

]


