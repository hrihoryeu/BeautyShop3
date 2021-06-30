from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
import urllib.request
import time
# Create your views here.


@login_required(login_url='/sign-in/')
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/created.html', {
                'order': order
            })
    else:
        form = OrderCreateForm
    return render(request, 'orders/create.html', {
        'cart': cart,
        'form': form
    })


def admin_panel(request):
    if request.method == 'POST':
        choose = request.POST['choose']
        if choose == 'products':
            f = open(f'files/products/product_{time.strftime("%y_%b_%d_%X")}.json', 'w')
            page = urllib.request.urlopen('http://127.0.0.1:8000/catalogue/api/products?format=json')
        elif choose == 'orders':
            f = open(f'files/orders/order_{time.strftime("%y_%b_%d_%X")}.json', 'w')
            page = urllib.request.urlopen('http://127.0.0.1:8000/catalogue/api/orders?format=json')
        pagetext = str(page.read())
        f.write(pagetext[2:-1])
        f.close()

    return render(request, 'orders/admin.html', {

    })
