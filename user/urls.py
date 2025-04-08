from django.urls import path
from .views import home_page,signup_view,login_view,logout_view,profile_view


urlpatterns=[
    path('',home_page,name='bosh_sahifa'),
    path('signup/',signup_view,name='signUp'),
    path('login/',login_view,name='login'),
    path('logut/',logout_view,name='logout'),
    path('profile/<int:id>/',profile_view,name='profile'),
]

