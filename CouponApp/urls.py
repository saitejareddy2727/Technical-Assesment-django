from django.urls import path
# from . import views
from .views import CartView,ApplyCouponView

urlpatterns = [
    path('cart_view/', CartView.as_view(), name='cart'),
    path('apply-coupon/', ApplyCouponView.as_view(), name='apply-coupon'),
]