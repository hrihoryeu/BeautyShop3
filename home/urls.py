from django.urls import path
from home import views

urlpatterns = [
    path('', views.shop_home, name='shop_home'),
]
