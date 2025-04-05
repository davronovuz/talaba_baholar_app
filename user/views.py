from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import UserRegisterForm,UserLoginForm
from .models import CustomUser




def signupview(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.password=make_password(form.cleaned_data["password1"])
            form.save()
            return redirect("login")

    else:
        form = UserRegisterForm()

    context={
        "form":form
    }
    return render(request,"signup.html",context)




def loginview(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=CustomUser.objects.filter(username=username).first()
            if user:
                if not user.check_password(password):
                    raise ValidationError("Parol xato")
            else:
                raise ValidationError("Bunday foydalanuvchi topilmadi")

            return redirect("home")

    else:
        form = UserLoginForm()

    context={
        "form":form
    }



    return render(request,"login.html",context)