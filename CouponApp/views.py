# 

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Coupon
from django.utils import timezone


class CartView(View):
    def get(self, request):
        cart = request.session.get('cart', {})
        coupon_code = request.session.get('coupon_code')
        total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

        if coupon_code:
            coupon = Coupon.objects.filter(code=coupon_code).first()
            if coupon and coupon.is_valid():
                discount_amount = (total_price * coupon.discount) / 100
                total_price -= discount_amount
                messages.success(request, f'Coupon applied: {coupon.discount}% off')
            else:
                messages.error(request, 'Invalid or expired coupon.')

        return render(request, 'store/cart_view.html', {
            'discount_amount':discount_amount,
            'cart': cart,
            'total_price': total_price,
            'coupon_code': coupon_code
        })

class ApplyCouponView(View):
    def post(self, request):
        coupon_code = request.POST.get('coupon_code')
        print(coupon_code)
        
        if coupon_code:
            # Retrieve the coupon object based on the code
            coupon = Coupon.objects.filter(code=coupon_code).first()
            print(coupon)
            
            if coupon and coupon.active and coupon.valid_from <= timezone.now() <= coupon.valid_to:
                # Apply the coupon
                request.session['coupon_code'] = coupon_code
                messages.success(request, 'Coupon applied successfully!')
            else:
                messages.error(request, 'Invalid or expired coupon.')
        else:
            messages.error(request, 'Please enter a coupon code.')

        return redirect('cart')
