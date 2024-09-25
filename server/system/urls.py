from django.urls import path
from .views import system_view
#from .views import 

urlpatterns = [
    path('', system_view, name = "system"),
]
