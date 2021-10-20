"""BeautyShop3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from easter_egg import views as easter_views

from django.contrib.auth.views import LoginView, LogoutView

from user_registration import views
from orders.views import admin_panel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-panel/', admin_panel, name='admin_panel'),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('catalogue/', include(('shop.urls', 'shop'), namespace='shop')),
    path('easter-egg/', easter_views.main, name='easter'),
    path('', include(('main.urls', 'main'), namespace='main')),
    # USER
    path('log-in/', views.login_view,
         name='beautyshop-log-in'),
    path('sign-out/', views.logout_view,
         name='beautyshop-sign-out'),
    path('sign-up/', views.beautyshop_sign_up, name='beautyshop-sign-up'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
