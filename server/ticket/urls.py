from django.urls import path
from .views import ticket_view, ticket_details

urlpatterns = [
    path('', ticket_view, name = "ticket"),
    path('<int:id>/', ticket_details, name='ticket_details'),
]
