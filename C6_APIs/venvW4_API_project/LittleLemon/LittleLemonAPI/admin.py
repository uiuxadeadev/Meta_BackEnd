from django.contrib import admin
from .models import Category, MenuItem, Cart, Order, OrderItem

# Register your models here.
for model in [Category, MenuItem, Cart, Order, OrderItem]:
    admin.site.register(model)
