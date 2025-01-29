from django.contrib import admin
from .models import Item_catg, Item

# Register your models here.
class Admin_catg_item(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("name","created", "updated")
    search_fields = ("name", "created", "updated")

class Admin_item(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    search_fields = ("name", "categories", "availability")

admin.site.register(Item_catg, Admin_catg_item)

admin.site.register(Item, Admin_item)
