from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .models import Order, Order_text
from shop_app.cart import Cart


# Create your views here.
@login_required (login_url = "/authentication_app/log_in")
def process_order (request):
    order = Order.objects.create(user = request.user)
    cart = Cart(request)
    order_text = list()

    for key, value in cart.cart.items():
        order_text.append(Order_text(
            item_id = key,
            quantity = value["quantity"],
            user = request.user,
            order = order
        ))

    #Insert into database
    Order_text.objects.bulk_create(order_text)

    send_mail_order(
        order = order,
        order_text = order_text,
        user_name = request.user.username,
        user_mail = request.user.email,
    )

    #Message for user
    messages.success(request, "Order correctly done!")
    cart.clean_cart()

    return redirect("../shop")


def send_mail_order(order, order_text, user_name, user_mail):
    recipient_list = [settings.NOTIFY_EMAIL]
    subject = "Order done in Board games shop"
    message = render_to_string("orders_app/order.html", {
        "order": order,
        "order_text": order_text,
        "user_name": user_name
    })

    message_text = strip_tags(message)

    send_mail(
        subject = subject,
        message = message_text,
        #Test with mailtrap
        from_email = user_mail,
        recipient_list = recipient_list,
        html_message = message)