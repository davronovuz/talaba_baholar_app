from django.urls import path
from .views import home_page,signup_view,login_view


urlpatterns=[
    path('',home_page,name='bosh_sahifa'),
    path('signup/',signup_view,name='signUp'),
    path('login/',login_view,name='login'),
]

