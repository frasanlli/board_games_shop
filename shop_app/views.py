from django.shortcuts import render
from .models import Item, Item_catg

# Create your views here.

def home (request):

    return render(request, "shop_app/home.html")

def shop (request):
    items = Item.objects.all()
    categories = Item_catg.objects.all()

    return render(request, "shop_app/shop.html",
                  {"items": items, "categories": categories})

def category_filter (request, category_id):
    category = Item_catg.objects.get(id = category_id)
    items = Item.objects.filter(categories = category)
    categories = Item_catg.objects.all()

    return render(request, "shop_app/category.html",
                  {"category": category, "items": items, "categories": categories})