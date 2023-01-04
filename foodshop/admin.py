from django.contrib import admin
from .models import Restaurant, Menu, Order, Cart,Category

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone','image_tag']
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['title', 'description',]

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_filter = ('restaurant',)
    ordering = ('price','name')
    list_display = ['name', 'restaurant', 'price','image_tag']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('-date',)
    list_filter = ('restaurant',)
    search_fields = ('customer',)
    list_display = ['customer', 'restaurant', 'menu', 'date']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_price']
