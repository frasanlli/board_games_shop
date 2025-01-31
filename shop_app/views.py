from django.shortcuts import render, redirect
from .models import Item, Item_catg
from .cart import Cart

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


def add_item (request, item_id):
    cart = Cart(request)
    item = Item.objects.get(id = item_id)

    cart.add(item)

    return redirect("shop")


def delete_item (request, item_id):
    cart = Cart(request)
    item = Item.objects.get(id = item_id)
    cart.delete(item)

    return redirect("shop")


def substract_item (request, item_id):
    cart = Cart(request)
    item = Item.objects.get(id = item_id)
    cart.substract(item)

    return redirect("shop")


def clean_cart (request):
    cart = Cart(request)
    cart.clean_cart()

    return redirect("shop")