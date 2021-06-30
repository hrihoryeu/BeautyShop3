from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product, Warehouse
from cart.cart import Cart
from cart.forms import CartAddProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/log-in/')
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if request.method == "POST":
        data = request.POST
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=int(data['quantity']),
                     update_quantity=cd['update'])
            quantity = product.warehouse.stock
            quantity -= int(data['quantity'])
            warehouse = Warehouse.objects.get(product=product)
            warehouse.stock = quantity
            warehouse.save()
    return redirect('cart:cart_detail')


@login_required(login_url='/log-in/')
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    warehouse = Warehouse.objects.get(product=product)
    quantity = cart.cart[str(product_id)]['quantity']
    warehouse.stock += quantity
    warehouse.save()
    cart.remove(product)
    return redirect('cart:cart_detail')


@login_required(login_url='/log-in/')
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/details.html', {
        'cart': cart
    })
