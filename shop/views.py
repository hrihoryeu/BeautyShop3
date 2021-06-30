from django.shortcuts import render, get_object_or_404
from shop.models import Product, Type, Brand, Warehouse
from orders.models import Order
from cart.forms import CartAddProductForm
from rest_framework.response import Response
from rest_framework.views import APIView
from shop.serializers import ProductSerializer, OrderSerializer

# Create your views here.


def product_list(request, brand_slug=None, type_slug=None):
    product_type = None
    brand = None
    product_types = Type.objects.all()
    brands = Brand.objects.all()
    products = Product.objects.filter(available=True)
    warehouse = Warehouse.objects.all()

    if type_slug:
        product_type = get_object_or_404(Type, slug=type_slug)
        products = products.filter(product_type=product_type)

    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)

    return render(request, 'shop/list.html', {
        'brand': brand,
        'brands': brands,
        'product_type': product_type,
        'product_types': product_types,
        'products': products,
        'warehouse': warehouse,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html', {
        'product': product,
        'cart_product_form': cart_product_form,
    })


class ProductView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            'products': serializer.data
        })


class OrderView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response({
            'products': serializer.data
        })
