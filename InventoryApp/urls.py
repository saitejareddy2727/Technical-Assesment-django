from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('api/products/<str:sku>/', ProductDetail.as_view(), name='product-detail'),
]
