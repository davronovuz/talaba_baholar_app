from django.shortcuts import render
from .models import Baho,Sinf,Fan
from user.models import CustomUser


#Bitta  o'quvchining barcha baholari

def student_all_grade(request,id):
    oquvchi=CustomUser.objects.get(id=id)
    baholar=Baho.objects.filter(oquvchi=oquvchi)

    context={
        "oquvchi":oquvchi,
        "baholar":baholar
    }
    return render(request,"oquvchi_baholar.html",context)