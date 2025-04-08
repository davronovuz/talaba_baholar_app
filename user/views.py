from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.views.generic import TemplateView
from django.contrib import messages


def home_page(request):
    return render(request, "home.html")


class HomePageView(TemplateView):
    template_name = "home.html"


def signup_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Formaning o'zida password set qilinadi
            messages.success(request, "Ro'yxatdan muvaffaqiyatli o'tdingiz! Endi tizimga kiring.")
            return redirect("login")
    else:
        form = UserRegisterForm()

    context = {
        "form": form
    }
    return render(request, "signup.html", context)


def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Xush kelibsiz, {username}!")
                return redirect("bosh_sahifa")  # "bosh_sahifa" o'rniga "home_page"
            else:
                messages.error(request, "Login yoki parol noto'g'ri!")
        else:
            messages.error(request, "Formani to'ldirishda xatolik!")
    else:
        form = UserLoginForm()

    context = {
        "form": form
    }
    return render(request, "login.html", context)