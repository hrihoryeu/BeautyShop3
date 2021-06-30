from django.contrib import admin
from shop.models import Type, Product, Brand, Warehouse

# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Type, TypeAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'establishment']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Brand, BrandAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product, ProductAdmin)


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ['product', 'stock']


admin.site.register(Warehouse, WarehouseAdmin)