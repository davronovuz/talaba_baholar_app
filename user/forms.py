from django.core.exceptions import ValidationError

from .models import CustomUser
from django import forms

class UserRegisterForm(forms.ModelForm):
    password1=forms.CharField(label="Parol kiriting",widget=forms.PasswordInput)
    password2=forms.CharField(label="Parolni tasdiqlang",widget=forms.PasswordInput)


    class Meta:
        model=CustomUser
        fields=("username","email","password1","password2")

    def clean_password1(self):
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Kiritilgan parollar bir biriga teng emas")


        return password1


class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        user=CustomUser.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise ValidationError("Parol xato")
        else:
            raise ValidationError("Bunday foydalanuvchi topilmadi")

        return self.cleaned_data





