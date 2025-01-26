from django.shortcuts import render

# Create your views here.

def home (request):

    return render(request, "shop_app/home.html")


def service (request):

    return render(request, "shop_app/service.html")


def shop (request):

    return render(request, "shop_app/shop.html")


def blog (request):

    return render(request, "shop_app/blog.html")


def contact (request):

    return render(request, "shop_app/contact.html")