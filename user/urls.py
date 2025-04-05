from django.urls import path
from .views import home_page,signupview,login_view


urlpatterns=[
    path('',home_page,name='bosh_sahifa'),
    path('signup/',signupview,name='signUp'),
    path('login/',login_view,name='login'),
]

