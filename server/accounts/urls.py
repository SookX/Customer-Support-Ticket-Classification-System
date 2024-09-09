from django.urls import path
from .views import user

urlpatterns = [
    path('', user, name='user'), # user url
    #path('login/', login, name='login'), # login url
]
