from django.shortcuts import render
from random import randint
from shop.models import Product

# Create your views here.


def shop_home(request):
    count = 0
    for _ in Product.objects.all():
        count += 1
    numbers = [randint(1, count - 1) for _ in range(3)]
    prod1 = Product.objects.get(id=numbers[0])
    prod2 = Product.objects.get(id=numbers[1])
    prod3 = Product.objects.get(id=numbers[2])
    print(prod1)
    print(prod2)
    print(prod3)
    return render(request, 'shop/home.html', {
        'prod1': prod1,
        'prod2': prod2,
        'prod3': prod3
    })
