from django.urls import path
from .views import system_view, system_details
#from .views import 

urlpatterns = [
    path('', system_view, name = "system"),
    path('<int:id>/', system_details, name='system_details'),
]
