from datetime import timezone, datetime

from django.db import models

from accounts.models import User
from django.utils.safestring import mark_safe


# Create your models here.
class Restaurant(models.Model):
    image=models.ImageField(upload_to="restau",default='default.png')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Restaurant {self.name} "

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))

    image_tag.short_description = 'Image'

class Category(models.Model):

    title=models.CharField(max_length=200)
    image_cat=models.ImageField(default='default.png',upload_to="cat_images")
    description = models.TextField(blank=True)
    active = models.BooleanField(default=False)


    def __str__(self):
        return self.title


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    image=models.ImageField(default="default_2.jpg",upload_to="menu_pictures")
    description=models.TextField(default='')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="menus")
    active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    date_add=models.DateTimeField(default=datetime.now)

    def image_tag(self):
        return mark_safe('<img src="{}" width="150" height="150" />'.format(self.image.url))

    image_tag.short_description = 'Image'

class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    customer = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orders = models.ManyToManyField(Order)
    total_price = models.IntegerField(default=0)


