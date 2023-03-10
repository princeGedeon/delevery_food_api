from django.contrib import admin
from .models import Restaurant, Menu, Order, Cart, Category, MenuOption, MenuOptionAssociation


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone','image_tag']
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['title', 'description',]


class MenuOptionAssociationInline(admin.TabularInline):
    model = MenuOptionAssociation

@admin.register(MenuOption)
class MenuOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuOptionAssociationInline]
    list_filter = ('restaurant',)
    ordering = ('price','name')
    list_display = ['name', 'restaurant', 'price','image_tag']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    ordering = ('-date','quantity')
    list_filter = ('restaurant','statut')
    search_fields = ('customer',)
    list_display = ['customer', 'restaurant', 'menu','quantity','date','statut']

