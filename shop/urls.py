from django.urls import path
from shop import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:brand_slug>/',
         views.product_list,
         name='product_list_by_category'),
    path('<slug:type_slug>/',
         views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/',
         views.product_detail,
         name='product_detail'),
    path('api/products', views.ProductView.as_view()),
    path('api/orders', views.OrderView.as_view())
]
