from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from InventoryApp.models import Product

def add_to_cart(request, sku):
    product = get_object_or_404(Product, sku=sku)
    cart = request.session.get('cart', {})

    quantity = int(request.POST.get('quantity', 1))
    if sku in cart:
        cart[sku]['quantity'] += quantity
    else:
        cart[sku] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': product.quantity_in_stock,
        }

    request.session['cart'] = cart
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    return render(request, 'store/cart.html', {'cart': cart, 'total_price': total_price})
