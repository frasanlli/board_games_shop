from django.contrib import admin

from .models import Order, Order_text

# Register your models here.

admin.site.register([Order, Order_text])