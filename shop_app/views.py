from django.shortcuts import render

# Create your views here.

def home (request):

    return render(request, "home.html")


def service (request):

    return render(request, "service.html")


def shop (request):

    return render(request, "blog.html")


def blog (request):

    return render(request, "blog.html")


def contact (request):

    return render(request, "contact.html")