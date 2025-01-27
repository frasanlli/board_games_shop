from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from shop_app.forms import Contact_form

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

    recipient_list = [settings.NOTIFY_EMAIL]

    if request.method == "POST":
        my_form = Contact_form(request.POST)

        if my_form.is_valid():
            form_info = my_form.cleaned_data
            send_mail(
                subject = form_info['subject'],
                message = form_info['message'],
                from_email = form_info.get('email', ''),
                recipient_list = recipient_list)

            return render(request, "thanks.html")

    else:
        my_form = Contact_form()

    return render(request, "shop_app/contact.html", {"form":my_form})