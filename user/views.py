from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import UserRegisterForm,UserLoginForm
from .models import CustomUser
from django.views import View
from django.views.generic import TemplateView



def home_page(request):
    return render(request,"home.html")

class HomePageView(TemplateView):
    template_name = "home.html"



def signupview(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.password=make_password(form.cleaned_data["password1"])
            user.save()
            return redirect("login")

    else:
        form = UserRegisterForm()

    context={
        "form":form
    }
    return render(request,"signup.html",context)


def login_view(request):
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("bosh_sahifa")
            else:
                form.add_error("Bunday foydalanuvchi yo'q")
    else:
        form=UserLoginForm()
    context={
        "form":form
    }
    return render(request,"login.html",context)



