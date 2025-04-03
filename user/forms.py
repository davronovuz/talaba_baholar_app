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






