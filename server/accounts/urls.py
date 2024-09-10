from django.urls import path
from .views import user, user_detail, login, register

urlpatterns = [
    path('', user, name='user'), # user url
    path('<int:id>/', user_detail, name='user_detail'),
    path('login/', login, name='login'), # login url
    path('register/', register, name='register'),
]
