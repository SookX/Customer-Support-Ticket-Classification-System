from django.urls import path
from .views import register, login

urlpatterns = [
    path('register/', register, name='register'), # register url
    path('login/', login, name='login'), # login url
]
