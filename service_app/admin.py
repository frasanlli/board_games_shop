from django.contrib import admin
from .models import Service

# Register your models here.

class Admin_service(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "content", "image", "created", "updated")
    search_fields = ("title", "content")

admin.site.register(Service, Admin_service)