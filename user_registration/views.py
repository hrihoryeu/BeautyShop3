from django.shortcuts import render, redirect, HttpResponseRedirect
from main import views
from user_registration.forms import UserForm, UserLogInForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from cart.models import OrderDetail
from shop.models import Product
from cart.cart import Cart
from django.db import IntegrityError

# Create your views here.


def beautyshop_sign_up(request):
    form = UserForm

    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)

            login(request, authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            ))

            return HttpResponseRedirect('/')
    return render(request, 'user_registration/beautyshop_sign_up.html', {
        'form': form,
    })


def login_view(request):
    form = UserLogInForm
    cart = Cart(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                print(f'id1 = {user.id}')
                json = OrderDetail.objects.get(user=username)
                for item in json.json:
                    product = Product.objects.get(id=item)
                    quantity = int(json.json[item])
                    print(f'product - {product}')
                    print(f'quantity - {quantity}')
                    cart.add(product=product,
                             quantity=int(quantity))
                return HttpResponseRedirect('/')
            except:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('beautyshop-log-in')

    return render(request, 'user_registration/beautyshop_log_in.html', {
        'form': form,
    })


def logout_view(request):
    cart = Cart(request)
    json = dict()
    for item in cart.cart:
        json.update({item: cart.cart[item]['quantity']})

    try:
        obj = OrderDetail.objects.get(user=request.user.username)
        obj.delete()
        OrderDetail.objects.create(user=request.user.username, json=json)
    except:
        OrderDetail.objects.create(user=request.user.username, json=json)

    logout(request)
    return HttpResponseRedirect('/')
'''    try:
        print(f' id = {request.user.id}')
        print(json)
        OrderDetail.objects.create(user=request.user.username, json=json)
    except:
        OrderDetail.objects.update(user=request.user.username, json=json)'''