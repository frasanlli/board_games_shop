from django.contrib import admin
from .models import Category, Post

# Register your models here.
class Admin_category(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("name","created", "updated")
    search_fields = ("name", "created", "updated")

class Admin_post(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    """list_display = ("title", "content", "image", "author",
                    "categories", "created", "updated")"""
    search_fields = ("title", "content")

admin.site.register(Category, Admin_category)

admin.site.register(Post, Admin_post)