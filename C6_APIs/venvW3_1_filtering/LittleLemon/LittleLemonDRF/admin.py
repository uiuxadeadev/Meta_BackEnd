from django.contrib import admin

# Register your models here.
from .models import Category
from .models import MenuItem

# Register your models here.
admin.site.register(Category)
admin.site.register(MenuItem)