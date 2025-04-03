from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import CustomUser


def signupview(request):
    form=UserRegisterForm()
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



