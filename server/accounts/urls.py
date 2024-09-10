from django.urls import path
from .views import user, user_detail

urlpatterns = [
    path('', user, name='user'), # user url
    path('<int:id>/', user_detail, name='user_detail'),
    #path('login/', login, name='login'), # login url
]
