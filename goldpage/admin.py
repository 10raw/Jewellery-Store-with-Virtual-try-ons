from django.contrib import admin

# Register your models here.
from .models import Order, OrderedItems, Products
admin.site.register(Products)
# admin.site.register(CartOrder)
# admin.site.register(CartOrderItems)
admin.site.register(Order)
admin.site.register(OrderedItems)