from django.contrib.auth.models import AbstractUser

from django.db import models


class CustomUser(AbstractUser):
    birth_date=models.DateTimeField(auto_now=True,null=True,blank=True,verbose_name="Tug'ilgan sana")
    addres=models.CharField(max_length=200,null=True,blank=True,verbose_name="Manzil")
    phone=models.CharField(max_length=15,null=True,blank=True,verbose_name="telefon raqam")
    avatar=models.ImageField(upload_to="avatar/",null=True,blank=True,verbose_name="Student rasmi")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"







