from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from contact_app.forms import Contact_form

# Create your views here.
def contact (request):

    recipient_list = [settings.NOTIFY_EMAIL]

    if request.method == "POST":
        my_form = Contact_form(request.POST)

        if my_form.is_valid():
            form_info = my_form.cleaned_data

            try:
                send_mail(
                    subject = form_info['subject'],
                    message = form_info['message'],
                    from_email = form_info.get('email', ''),
                    recipient_list = recipient_list)

                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?error")
    else:
        my_form = Contact_form()

    return render(request, "contact_app/contact.html", {"form":my_form})