from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('accounts.urls')), # main url for the 
    path('api/ticket/', include('ticket.urls')),
    path('api/system/', include('system.urls')),
]
