from django.db import models

from user.models import CustomUser


class Sinf(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    oquvchi=models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name

class Fan(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    sinf=models.ForeignKey(Sinf,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Baho(models.Model):
    fan=models.ForeignKey(Fan,on_delete=models.CASCADE,related_name='baholar')
    oquvchi=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="baholar")
    baho=models.IntegerField(default=2)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.oquvchi}-{self.fan}-{self.baho}"









