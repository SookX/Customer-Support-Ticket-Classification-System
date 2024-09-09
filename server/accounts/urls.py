from django.urls import path
from .views import register

urlpatterns = [
    path('', register, name='register'), # register url
    #path('login/', login, name='login'), # login url
]
