from django.core.exceptions import ValidationError
from django import forms
from .models import CustomUser

class UserRegisterForm(forms.ModelForm):  #Forms ModelForm
    password1 = forms.CharField(label="Parol kiriting", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Parolni tasdiqlang", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "password1", "password2")

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Kiritilgan parollar bir biriga teng emas")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username kiriting", max_length=250)
    password = forms.CharField(label="Parol kiriting", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if username and password:
            try:
                user = CustomUser.objects.get(username=username)
                if not user.check_password(password):
                    raise ValidationError("Parol xato")
            except CustomUser.DoesNotExist:
                raise ValidationError("Foydalanuvchi topilmadi")

        return cleaned_data
