from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

class Register (View):

    def get (self, request):
        form = UserCreationForm()

        return render(request, "authentication_app/register.html", {"form": form})

    #register user un db
    def post (self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("home")

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "authentication_app/register.html", {"form": form})

def log_in(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username,
                                password = password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                for msg in form.error_messages:
                    messages.error(request, form.error_messages[msg])

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages)

    return render(request, "authentication_app/log_in.html", {"form": form})

def log_out(request):
    logout(request)

    return redirect("home")