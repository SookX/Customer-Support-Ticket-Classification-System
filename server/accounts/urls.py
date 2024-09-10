from django.urls import path
from .views import user, delete_user

urlpatterns = [
    path('', user, name='user'), # user url
    path('<int:id>/', delete_user, name='delete_user'), # Endpoint for deleting a user
    #path('login/', login, name='login'), # login url
]
