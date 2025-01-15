from django.contrib import admin
from .models import CustomerDB, ProductDB, CartDB, PlacedOrderDB
# Register your models here.

@admin.register(CustomerDB)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(ProductDB)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tag' , 'selling_price', 'discounted_price', 'description', 'brand', 'category', 'product_image']

@admin.register(CartDB)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(PlacedOrderDB)
class PlacedOrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'customer', 'product', 'quantity', 'order_placed_date', 'order_delivered_date', 'order_cancel_date', 'status']
