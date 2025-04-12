from django.urls import path
from .views import student_all_grade

urlpatterns=[
    path('<int:id>/',student_all_grade,name='bahos'),
]