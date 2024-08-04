from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<str:sku>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart_detail, name='cart_detail'),
]
